#!/usr/bin/env python3
"""PAGES의 산출물 목록을 읽어 samples/w{week}d{day}/README.md 및 samples/w{week}d{day}/md/ 스텁을 생성."""
from __future__ import annotations

import ast
import os
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROG_ROOT = SCRIPT_DIR.parent
GEN = SCRIPT_DIR / "python generate_pages.py"
SAMPLES = PROG_ROOT / "intern-documents" / "docs_output" / "samples"

# 최소 유효 PNG (1×1 투명 픽셀)
MINI_PNG = bytes.fromhex(
    "89504e470d0a1a0a0000000d49484452000000010000000108060000001f15c489"
    "0000000a49444154789c63000100000500001d0a2db40000000049454e44ae426082"
)


def parse_pages():
    src = GEN.read_text(encoding="utf-8")
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
            if node.targets[0].id != "PAGES":
                continue
            for elt in node.value.elts:
                w, d = elt.elts[0].value, elt.elts[1].value
                title = elt.elts[3].value
                date = elt.elts[2].value
                outs = ast.literal_eval(ast.unparse(elt.elts[9]))
                yield w, d, date, title, outs


def strip_desc(entry: str) -> str:
    entry = entry.strip()
    if " — " in entry:
        entry = entry.split(" — ", 1)[0].strip()
    entry = re.sub(r"\s*\([^)]*\)\s*$", "", entry).strip()
    if " 또는 " in entry:
        # 샘플은 편집 가능한 쪽(.md) 우선
        parts = [p.strip() for p in entry.split(" 또는 ")]
        md_pref = [p for p in parts if p.endswith(".md")]
        if md_pref:
            entry = md_pref[0]
        else:
            entry = parts[0]
    return entry


def write_minimal_png(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(MINI_PNG)


def stub_md(path: Path, heading: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"# {heading}\n\n> 샘플(예시) 문서입니다. 본인 이름·날짜·내용으로 바꿔 사용하세요.\n\n{body}\n",
        encoding="utf-8",
    )


def stub_py(path: Path, desc: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(
            f'"""{desc} — 샘플 스켈레톤."""\n\n\ndef main():\n    print("ok")\n\n\n'
            'if __name__ == "__main__":\n    main()\n',
            encoding="utf-8",
        )


def stub_ipynb(path: Path) -> None:
    import json

    nb = {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {},
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["# 데이터 분석 노트 (샘플)\n", "\n", "아래 셀부터 작성합니다.\n"],
            },
            {
                "cell_type": "code",
                "metadata": {},
                "source": ["import pandas as pd\n", "print(pd.__version__)\n"],
                "outputs": [],
                "execution_count": None,
            },
        ],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")


def make_readme(w: int, d: int, date: str, title: str, outs: list[str]) -> str:
    lines = [
        f"# W{w} Day{d} 산출물 샘플 — {title}",
        "",
        f"- **일자:** {date}",
        f"- **프로그램 페이지:** `intern-program/week{w}/day{d}.html`",
        "",
        "## 오늘 제출·보관할 파일",
        "",
    ]
    for o in outs:
        lines.append(f"- `{strip_desc(o)}`")
    lines.extend(
        [
            "",
            "## 작성 가이드",
            "",
            "1. 위 목록의 파일을 이 폴더에 두거나, 팀 규칙에 맞는 경로에 둡니다.",
            "2. 민감·내부 정보는 넣지 말고, 공개 가능한 샘플·가명으로 대체합니다.",
            "3. 멘토 제출 전 파일명·버전을 한 번 더 확인합니다.",
            "",
        ]
    )
    return "\n".join(lines)


def create_artifact(folder: Path, raw_entry: str, w: int, d: int, title: str) -> None:
    name = strip_desc(raw_entry)
    if not name or name.lower() == "없음":
        return
    if name.endswith("/"):
        sub = folder / name.rstrip("/")
        sub.mkdir(parents=True, exist_ok=True)
        (sub / "README.md").write_text(
            f"# {name.rstrip('/')}\n\n하위에 링크·내보낸 파일·스크린샷을 둡니다. (W{w}D{d})\n",
            encoding="utf-8",
        )
        return

    path = folder / name
    ext = path.suffix.lower()
    stem = path.stem

    if ext == ".md":
        if path.exists() and folder.parent.name in ("w1d2", "w1d1") and path.name != "README.md":
            return  # 기존 상세 샘플 유지
        stub_md(
            path,
            f"{stem}",
            f"**일정:** W{w} D{d} — {title}\n\n## 내용\n\n- 항목 1\n- 항목 2\n\n## 참고\n\n",
        )
    elif ext == ".py":
        stub_py(path, f"W{w}D{d} {title}")
    elif ext == ".ipynb":
        stub_ipynb(path)
    elif ext == ".pdf":
        stub_md(
            path.with_suffix(".md"),
            f"{stem} (PDF 안내)",
            "PDF는 Word/Markdown에서 내보내 `"
            + name
            + "` 이름으로 저장합니다. 이 `.md`는 샘플용 안내입니다.\n",
        )
    elif ext == ".png":
        write_minimal_png(path)
    elif ext == ".pptx":
        stub_md(
            path.with_suffix(".md"),
            f"{stem} (슬라이드 목차 샘플)",
            "## 슬라이드 목차 (예시)\n\n1. 표지\n2. 배경\n3. 방법\n4. 데모\n5. 성과\n6. 한계\n7. Q&A\n",
        )
    elif ext == ".mp4":
        stub_md(
            path.with_suffix(".md"),
            f"{stem} (데모 영상 안내)",
            "실제로는 화면 녹화 파일(`.mp4`)을 이 이름으로 저장합니다.\n",
        )
    else:
        stub_md(
            path.with_suffix(path.suffix + ".md"),
            f"{name}",
            f"확장자 `{ext}` 샘플 자리입니다. W{w}D{d} 산출물로 교체하세요.\n",
        )


def write_master_index(rows: list[tuple[int, int, str]]) -> None:
    p = SAMPLES / "README.md"
    lines = [
        "# 일자별 산출물 샘플 (40일)",
        "",
        "각 폴더는 해당 일자의 **산출물 예시**와 `README.md` 가이드를 담습니다.",
        "",
        "| 주차·일 | 폴더 |",
        "|----------|------|",
    ]
    for w, d, title in rows:
        lines.append(f"| W{w} D{d} | [w{w}d{d}/](w{w}d{d}/README.md) — {title} |")
    lines.append("")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows: list[tuple[int, int, str]] = []
    for w, d, date, title, outs in parse_pages():
        day_dir = SAMPLES / f"w{w}d{d}"
        folder = day_dir / "md"
        day_dir.mkdir(parents=True, exist_ok=True)
        folder.mkdir(parents=True, exist_ok=True)
        readme = make_readme(w, d, date, title, outs)
        (day_dir / "README.md").write_text(readme, encoding="utf-8")
        for raw in outs:
            try:
                create_artifact(folder, raw, w, d, title)
            except OSError as e:
                print("skip", folder, raw, e)
        rows.append((w, d, title))
        print(f"OK w{w}d{d} ({len(outs)} outputs)")
    rows.sort(key=lambda x: (x[0], x[1]))
    write_master_index(rows)
    print("Master index:", SAMPLES / "README.md")


if __name__ == "__main__":
    main()
