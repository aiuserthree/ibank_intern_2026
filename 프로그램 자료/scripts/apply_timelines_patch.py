#!/usr/bin/env python3
"""generate_pages.py의 인라인 타임라인을 TIMELINES[(w,d)] 참조로 바꾸고 extra를 sample_extra_html로 통일."""
from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PATH = ROOT / "python generate_pages.py"


def main() -> None:
    src = PATH.read_text(encoding="utf-8")
    tree = ast.parse(src)
    lines = src.splitlines(keepends=True)

    replacements: list[tuple[int, int, str]] = []

    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not isinstance(node.targets[0], ast.Name) or node.targets[0].id != "PAGES":
            continue
        for elt in node.value.elts:
            w, d = elt.elts[0].value, elt.elts[1].value
            tl, ex = elt.elts[6], elt.elts[11]
            replacements.append(
                (tl.lineno, tl.end_lineno, f"   TIMELINES[({w}, {d})],\n")
            )
            replacements.append(
                (ex.lineno, ex.end_lineno, f"   sample_extra_html({w}, {d}),\n")
            )

    replacements.sort(key=lambda x: -x[0])

    for start, end, new_text in replacements:
        del lines[start - 1 : end]
        lines.insert(start - 1, new_text)

    new_src = "".join(lines)

    marker = "# ══════════════════════════════════════════════════════════════\n# 전체 페이지 데이터"
    insert_block = '''from timelines import TIMELINES

def sample_extra_html(week, day):
    folder = f"w{week}d{day}"
    return (
        '<div class="output-box" style="margin-bottom:28px;border-color:#7c4dff55;">'
        f'<h3>{OUT_SVG} 산출물 샘플 문서 (참고용)</h3>'
        '<p style="font-size:.88rem;color:var(--muted);margin-bottom:12px;line-height:1.6;">'
        f'<strong>W{week} Day{day}</strong> 예시 문서입니다. 경로: '
        f'<code>intern-documents/docs_output/samples/{folder}/</code> — 복사해 본인 환경에 맞게 수정하세요.'
        '</p>'
        '<ul style="list-style:none;font-size:.88rem;color:var(--text);line-height:1.85;">'
        '<li style="display:flex;align-items:flex-start;gap:8px;">'
        '<span style="color:#40c4ff;">→</span>'
        f'<span><a href="../../intern-documents/docs_output/samples/{folder}/README.md" '
        'style="color:var(--primary);font-weight:600;">README.md</a> — '
        '오늘 산출물 목록·작성 가이드·샘플 파일</span></li></ul></div>'
    )

'''

    if "from timelines import TIMELINES" not in new_src:
        if marker not in new_src:
            raise SystemExit("marker not found for insertion")
        new_src = new_src.replace(marker, insert_block + marker, 1)

    PATH.write_text(new_src, encoding="utf-8")
    print("Patched:", PATH)


if __name__ == "__main__":
    main()
