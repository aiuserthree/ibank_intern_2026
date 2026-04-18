import os

output_dir = "인턴과제_슬라이드"
os.makedirs(output_dir, exist_ok=True)

common_style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
        font-family: 'Noto Sans KR', sans-serif;
        background: #1A1A2E;
        color: #fff;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        padding: 24px 20px 28px;
        gap: 20px;
    }

    .slide {
        width: 1280px;
        height: 720px;
        background: #1A1A2E;
        border-radius: 12px;
        padding: 48px 56px;
        position: relative;
        overflow: hidden;
    }

    .accent-line {
        width: 60px;
        height: 3px;
        border-radius: 2px;
        margin-bottom: 12px;
    }

    .badge {
        display: inline-block;
        padding: 4px 20px;
        border-radius: 6px;
        font-size: 13px;
        font-weight: 700;
        color: #fff;
        margin-right: 12px;
    }

    .header-row {
        display: flex;
        align-items: center;
        margin-bottom: 8px;
    }

    .header-date {
        font-size: 14px;
        color: #B0B0C0;
    }

    .title {
        font-size: 28px;
        font-weight: 900;
        color: #fff;
        margin-bottom: 6px;
    }

    .card {
        background: #16213E;
        border-radius: 12px;
        padding: 24px 28px;
    }

    .card-time {
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .card-title {
        font-size: 16px;
        font-weight: 700;
        color: #fff;
        margin-bottom: 12px;
    }

    .card-list {
        list-style: none;
        padding: 0;
    }

    .card-list li {
        font-size: 12.5px;
        color: #B0B0C0;
        padding: 3px 0;
        padding-left: 16px;
        position: relative;
        line-height: 1.6;
    }

    .card-list li::before {
        content: '•';
        position: absolute;
        left: 0;
        color: #B0B0C0;
    }

    .checklist-bar {
        position: absolute;
        bottom: 36px;
        left: 56px;
        right: 56px;
        background: #0D2B45;
        border-radius: 10px;
        padding: 16px 24px;
    }

    .checklist-label {
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .checklist-items {
        font-size: 13px;
        color: #fff;
        line-height: 1.7;
    }

    .three-col {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 20px;
    }

    .two-col {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
    }

    .two-col-wide-right {
        display: grid;
        grid-template-columns: 47% 50%;
        gap: 3%;
    }

    .highlight-banner {
        border-radius: 8px;
        padding: 12px 24px;
        font-size: 15px;
        font-weight: 700;
        color: #fff;
        margin-bottom: 20px;
    }

    .flow-num {
        font-size: 14px;
        font-weight: 700;
        margin-right: 10px;
    }

    .flow-row {
        display: flex;
        align-items: center;
        padding: 6px 0;
    }

    .flow-text {
        font-size: 14px;
        color: #B0B0C0;
    }

    .sub-label {
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .rfp-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 4px 40px;
    }

    .rfp-grid li {
        font-size: 12px;
    }

    .slide-nav {
        flex-shrink: 0;
        display: flex;
        gap: 14px;
        align-items: center;
        background: rgba(22, 33, 62, 0.96);
        border: 1px solid rgba(0, 210, 255, 0.28);
        border-radius: 999px;
        padding: 10px 22px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.45);
        backdrop-filter: blur(8px);
    }

    .slide-nav .nav-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-width: 100px;
        padding: 8px 16px;
        border-radius: 8px;
        font-size: 14px;
        font-weight: 700;
        text-decoration: none;
        color: #fff;
        background: #0D2B45;
        border: 1px solid rgba(0, 210, 255, 0.35);
        transition: background 0.15s, border-color 0.15s;
    }

    .slide-nav a.nav-btn:hover {
        background: #16213E;
        border-color: #00D2FF;
    }

    .slide-nav .nav-btn.disabled {
        opacity: 0.38;
        cursor: not-allowed;
        border-color: rgba(255, 255, 255, 0.12);
        background: rgba(13, 43, 69, 0.5);
    }

    .slide-nav .nav-page {
        font-size: 13px;
        font-weight: 700;
        color: #B0B0C0;
        padding: 0 6px;
        user-select: none;
    }

    .slide-nav button.nav-btn {
        font-family: inherit;
        cursor: pointer;
    }

    .toc-overlay {
        position: fixed;
        inset: 0;
        background: rgba(0, 0, 0, 0.55);
        z-index: 200;
    }

    .toc-panel {
        position: fixed;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        width: min(420px, calc(100vw - 32px));
        max-height: min(520px, calc(100vh - 48px));
        overflow: hidden;
        display: flex;
        flex-direction: column;
        background: #16213E;
        border: 1px solid rgba(0, 210, 255, 0.35);
        border-radius: 14px;
        box-shadow: 0 24px 80px rgba(0, 0, 0, 0.55);
        z-index: 201;
    }

    /* HTML hidden 속성은 author CSS의 display보다 약해질 수 있어 반드시 숨김 처리 */
    .toc-overlay[hidden],
    .toc-panel[hidden] {
        display: none !important;
    }

    .toc-panel-head {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 18px 20px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        flex-shrink: 0;
    }

    .toc-panel-head h2 {
        font-size: 17px;
        font-weight: 800;
        color: #fff;
    }

    .toc-close {
        width: 36px;
        height: 36px;
        border: none;
        border-radius: 8px;
        background: #0D2B45;
        color: #fff;
        font-size: 22px;
        line-height: 1;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .toc-close:hover {
        background: #1a3d5c;
    }

    .toc-list {
        list-style: none;
        margin: 0;
        padding: 12px 14px 16px;
        overflow-y: auto;
    }

    .toc-item {
        margin: 0;
        padding: 0;
    }

    .toc-item a,
    .toc-item span {
        display: block;
        padding: 12px 14px;
        border-radius: 10px;
        font-size: 14px;
        font-weight: 600;
        line-height: 1.45;
        text-decoration: none;
        color: #fff;
        border: 1px solid transparent;
    }

    .toc-item a:hover {
        background: rgba(0, 210, 255, 0.12);
        border-color: rgba(0, 210, 255, 0.35);
    }

    .toc-item.toc-current span {
        color: #00D2FF;
        background: rgba(0, 210, 255, 0.12);
        border-color: rgba(0, 210, 255, 0.45);
        cursor: default;
    }
</style>
"""

# (파일명, 목록에 표시할 제목)
SLIDE_TOC = [
    ("01_표지.html", "01 · 표지"),
    ("02_전체흐름.html", "02 · 전체 흐름"),
    ("03_월요일_4월20일.html", "03 · 월요일 (4/20) · 학습 데이터 구축"),
    ("04_화요일_4월21일.html", "04 · 화요일 (4/21) · 벡터 DB + RFP 분석"),
    ("05_수요일_4월22일.html", "05 · 수요일 (4/22) · 제안서 생성 로직"),
    ("06_목요일_4월23일.html", "06 · 목요일 (4/23) · UI + 파일 출력"),
    ("07_금요일_4월24일.html", "07 · 금요일 (4/24) · 정리 및 발표"),
    ("08_산출물_유의사항.html", "08 · 산출물 · 유의사항"),
]


def toc_panel_html(current_filename):
    lines = []
    for href, label in SLIDE_TOC:
        if href == current_filename:
            lines.append(f'        <li class="toc-item toc-current"><span>{label}</span></li>')
        else:
            lines.append(f'        <li class="toc-item"><a href="{href}">{label}</a></li>')
    items_html = "\n".join(lines)
    return f"""<div class="toc-overlay" id="toc-overlay" hidden></div>
<div class="toc-panel" id="toc-panel" role="dialog" aria-modal="true" aria-labelledby="toc-title" hidden>
    <div class="toc-panel-head">
        <h2 id="toc-title">슬라이드 목록</h2>
        <button type="button" class="toc-close" id="toc-close-btn" aria-label="목록 닫기">×</button>
    </div>
    <ol class="toc-list">
{items_html}
    </ol>
</div>"""


def nav_block(prev_href, next_href, page_num, total=8, current_filename="01_표지.html"):
    prev_el = (
        f'<a class="nav-btn nav-prev" href="{prev_href}">← 이전</a>'
        if prev_href
        else '<span class="nav-btn nav-prev disabled" aria-disabled="true">← 이전</span>'
    )
    next_el = (
        f'<a class="nav-btn nav-next" href="{next_href}">다음 →</a>'
        if next_href
        else '<span class="nav-btn nav-next disabled" aria-disabled="true">다음 →</span>'
    )
    toc = toc_panel_html(current_filename)
    return f"""<nav class="slide-nav" aria-label="슬라이드 이동">
<button type="button" class="nav-btn toc-open" id="toc-open-btn" aria-expanded="false" aria-controls="toc-panel">목록</button>
{prev_el}
<span class="nav-page">{page_num} / {total}</span>
{next_el}
</nav>
{toc}
<script>
(function () {{
  var tocBtn = document.getElementById("toc-open-btn");
  var overlay = document.getElementById("toc-overlay");
  var panel = document.getElementById("toc-panel");
  var closeBtn = document.getElementById("toc-close-btn");

  function tocOpen() {{
    if (!overlay || !panel || !tocBtn) return;
    overlay.removeAttribute("hidden");
    panel.removeAttribute("hidden");
    tocBtn.setAttribute("aria-expanded", "true");
    document.body.style.overflow = "hidden";
  }}

  function tocClose() {{
    if (!overlay || !panel || !tocBtn) return;
    overlay.setAttribute("hidden", "");
    panel.setAttribute("hidden", "");
    tocBtn.setAttribute("aria-expanded", "false");
    document.body.style.overflow = "";
  }}

  if (tocBtn) tocBtn.addEventListener("click", function () {{
    if (panel && panel.hasAttribute("hidden")) tocOpen(); else tocClose();
  }});
  if (overlay) overlay.addEventListener("click", tocClose);
  if (closeBtn) closeBtn.addEventListener("click", tocClose);

  document.addEventListener("keydown", function (e) {{
    var tocVisible = panel && !panel.hasAttribute("hidden");
    if (e.key === "Escape") {{
      if (tocVisible) {{
        e.preventDefault();
        tocClose();
      }}
      return;
    }}
    if (tocVisible) return;
    if (e.key === "ArrowLeft" || e.key === "PageUp") {{
      var p = document.querySelector("a.nav-prev");
      if (p) {{ e.preventDefault(); p.click(); }}
    }}
    if (e.key === "ArrowRight" || e.key === "PageDown") {{
      var n = document.querySelector("a.nav-next");
      if (n) {{ e.preventDefault(); n.click(); }}
    }}
  }});
}})();
</script>"""


# ═══════════════════════════════════════
# 슬라이드 1 — 표지
# ═══════════════════════════════════════
cover = f"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8"><title>표지</title>{common_style}
</head><body>
<div class="slide">
    <div class="accent-line" style="background:#00D2FF; margin-top:80px;"></div>
    <div class="title" style="font-size:40px; margin-bottom:4px;">AI 기반 제안서 자동 생성 에이전트</div>
    <div style="font-size:26px; color:#00D2FF; margin-bottom:36px; font-weight:400;">1주 스프린트 과제</div>

    <div style="color:#B0B0C0; font-size:15px; line-height:2;">
        기간 &nbsp;|&nbsp; 4월 20일(월) ~ 4월 24일(금)<br>
        시간 &nbsp;|&nbsp; 매일 오후 1시 ~ 6시 (일 5시간, 총 25시간)<br>
        도구 &nbsp;|&nbsp; Cursor, GenSpark, 기타 자유
    </div>

    <div class="card" style="position:absolute; bottom:48px; left:56px; right:56px;">
        <div style="font-size:12px; color:#00D2FF; font-weight:700; margin-bottom:6px;">MISSION</div>
        <div style="font-size:13px; color:#B0B0C0; line-height:1.7;">
            우리 회사의 기존 제안서(PPT, PDF) 10~20건을 AI에게 학습시키고, 고객사 RFP를 분석하여<br>
            기존 제안서의 스타일과 구조를 반영한 제안서 초안을 자동 생성하는 에이전트를 만들어라.
        </div>
    </div>
</div>
</body></html>"""


# ═══════════════════════════════════════
# 슬라이드 2 — 전체 흐름
# ═══════════════════════════════════════
flow = f"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8"><title>전체 흐름</title>{common_style}
<style>
    .flow-card {{
        background: #16213E;
        border-radius: 12px;
        padding: 28px 24px;
        text-align: left;
    }}
    .flow-card .num {{
        font-size: 36px;
        font-weight: 900;
        margin-bottom: 12px;
    }}
    .flow-card .ftitle {{
        font-size: 18px;
        font-weight: 700;
        color: #fff;
        margin-bottom: 10px;
    }}
    .flow-card .fdesc {{
        font-size: 13px;
        color: #B0B0C0;
        line-height: 1.7;
    }}
    .flow-grid {{
        display: grid;
        grid-template-columns: 1fr auto 1fr auto 1fr auto 1fr;
        gap: 0;
        align-items: center;
        margin-top: 24px;
    }}
    .flow-arrow {{
        font-size: 24px;
        color: #B0B0C0;
        text-align: center;
        padding: 0 8px;
    }}
    .day-bar {{
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 12px;
        position: absolute;
        bottom: 40px;
        left: 56px;
        right: 56px;
    }}
    .day-chip {{
        border-radius: 8px;
        padding: 12px 16px;
    }}
    .day-chip .dday {{ font-size: 12px; font-weight: 700; color: #fff; }}
    .day-chip .ddesc {{ font-size: 11px; color: #fff; opacity: 0.85; margin-top: 2px; }}
</style>
</head><body>
<div class="slide">
    <div class="accent-line" style="background:#00D2FF;"></div>
    <div class="title">전체 흐름</div>

    <div class="flow-grid">
        <div class="flow-card">
            <div class="accent-line" style="background:#00D2FF; width:40px;"></div>
            <div class="num" style="color:#00D2FF;">01</div>
            <div class="ftitle">RFP 분석</div>
            <div class="fdesc">고객사 RFP 업로드<br>요구사항 자동 추출 및 구조화</div>
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-card">
            <div class="accent-line" style="background:#7B2FFF; width:40px;"></div>
            <div class="num" style="color:#7B2FFF;">02</div>
            <div class="ftitle">유사 제안서 검색</div>
            <div class="fdesc">학습된 기존 제안서에서<br>참고할 내용 탐색</div>
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-card">
            <div class="accent-line" style="background:#FFA500; width:40px;"></div>
            <div class="num" style="color:#FFA500;">03</div>
            <div class="ftitle">제안서 초안 생성</div>
            <div class="fdesc">RFP 요구사항 + 기존 스타일<br>기반으로 섹션별 작성</div>
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-card">
            <div class="accent-line" style="background:#00FF88; width:40px;"></div>
            <div class="num" style="color:#00FF88;">04</div>
            <div class="ftitle">파일 출력</div>
            <div class="fdesc">Word 또는 PPT로<br>내보내기</div>
        </div>
    </div>

    <div class="day-bar">
        <div class="day-chip" style="background:#00D2FF;"><div class="dday">4/20 (월)</div><div class="ddesc">데이터 구축</div></div>
        <div class="day-chip" style="background:#7B2FFF;"><div class="dday">4/21 (화)</div><div class="ddesc">DB + RFP분석</div></div>
        <div class="day-chip" style="background:#FFA500;"><div class="dday">4/22 (수)</div><div class="ddesc">생성 로직</div></div>
        <div class="day-chip" style="background:#FF6B9D;"><div class="dday">4/23 (목)</div><div class="ddesc">UI + 출력</div></div>
        <div class="day-chip" style="background:#00FF88; color:#1A1A2E;"><div class="dday" style="color:#1A1A2E;">4/24 (금)</div><div class="ddesc" style="color:#1A1A2E;">발표</div></div>
    </div>
</div>
</body></html>"""


# ═══════════════════════════════════════
# 슬라이드 3 — 월요일
# ═══════════════════════════════════════
mon = f"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8"><title>4/20 월요일</title>{common_style}
</head><body>
<div class="slide">
    <div class="header-row">
        <div class="badge" style="background:#00D2FF;">MON</div>
        <div class="header-date">4/20 (월) &nbsp;오후 1시~6시</div>
    </div>
    <div class="title">기존 제안서 학습 데이터 구축</div>
    <div class="accent-line" style="background:#00D2FF; width:120px; margin-bottom:24px;"></div>

    <div class="three-col">
        <div class="card">
            <div class="card-time" style="color:#00D2FF;">1:00 ~ 2:00</div>
            <div class="card-title">제안서 선별 및 메타데이터 정리</div>
            <ul class="card-list">
                <li>학습에 사용할 기존 제안서 10~20건 선별</li>
                <li>품질이 좋고 유형이 다양한 것 위주로 선택</li>
                <li>파일별 프로젝트 유형, 고객사, 작성 시기 정리</li>
            </ul>
        </div>
        <div class="card">
            <div class="card-time" style="color:#00D2FF;">2:00 ~ 4:00</div>
            <div class="card-title">텍스트 자동 추출 스크립트 개발</div>
            <ul class="card-list">
                <li>PPT → python-pptx / PDF → PyMuPDF, pdfplumber</li>
                <li>Cursor 활용하여 빠르게 스크립트 작성</li>
                <li>추출 결과 검증 및 오류 처리</li>
            </ul>
        </div>
        <div class="card">
            <div class="card-time" style="color:#00D2FF;">4:00 ~ 6:00</div>
            <div class="card-title">제안서 패턴 분석 + 청킹 착수</div>
            <ul class="card-list">
                <li>공통 목차 구조, 톤앤매너, 자주 쓰는 표현 분석</li>
                <li>→ 수요일 프롬프트 설계의 핵심 재료</li>
                <li>섹션 단위(회사소개, 수행방안, 일정 등) 청킹 시작</li>
            </ul>
        </div>
    </div>

    <div class="checklist-bar">
        <div class="checklist-label" style="color:#00D2FF;">퇴근 전 체크리스트</div>
        <div class="checklist-items">
            ☐ &nbsp;제안서 10건 이상 텍스트 추출 완료 &nbsp;&nbsp;&nbsp;&nbsp;
            ☐ &nbsp;제안서 패턴 분석 메모 작성 완료 &nbsp;&nbsp;&nbsp;&nbsp;
            ☐ &nbsp;청킹 작업 착수
        </div>
    </div>
</div>
</body></html>"""


# ═══════════════════════════════════════
# 슬라이드 4 — 화요일
# ═══════════════════════════════════════
tue = f"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8"><title>4/21 화요일</title>{common_style}
</head><body>
<div class="slide">
    <div class="header-row">
        <div class="badge" style="background:#7B2FFF;">TUE</div>
        <div class="header-date">4/21 (화) &nbsp;오후 1시~6시</div>
    </div>
    <div class="title">벡터 DB 구축 + RFP 분석 로직 개발</div>
    <div class="accent-line" style="background:#7B2FFF; width:120px; margin-bottom:20px;"></div>

    <div class="two-col" style="margin-bottom:16px;">
        <div class="card">
            <div class="card-time" style="color:#7B2FFF;">1:00 ~ 2:30</div>
            <div class="card-title">벡터 DB 구축 및 검색 테스트</div>
            <ul class="card-list">
                <li>월요일 청킹 작업 마무리 → ChromaDB에 임베딩 저장</li>
                <li>임베딩 모델 선정 (GenSpark로 빠르게 조사)</li>
                <li>자연어 검색 테스트로 검색 품질 확인</li>
            </ul>
        </div>
        <div class="card">
            <div class="card-time" style="color:#7B2FFF;">2:30 ~ 6:00</div>
            <div class="card-title">RFP 분석 모듈 개발 ★ 핵심</div>
            <ul class="card-list">
                <li>RFP 업로드 → AI가 요구사항을 자동 추출·구조화</li>
                <li>LLM 기반 문맥 이해 방식으로 구현</li>
                <li>추출 결과를 구조화된 JSON으로 출력</li>
            </ul>
        </div>
    </div>

    <div class="card" style="padding:18px 24px;">
        <div class="sub-label" style="color:#7B2FFF;">RFP에서 추출해야 할 항목</div>
        <ul class="card-list rfp-grid">
            <li>프로젝트명 및 발주 기관</li>
            <li>예산 범위</li>
            <li>사업 목적 및 배경</li>
            <li>평가 기준 및 배점</li>
            <li>핵심 요구사항 목록 (기능, 기술, 인력)</li>
            <li>제안서 작성 지침 (페이지 제한, 목차 지정)</li>
            <li>납기 및 일정 조건</li>
            <li>필수 포함 사항 및 제약 조건</li>
        </ul>
    </div>

    <div class="checklist-bar">
        <div class="checklist-label" style="color:#7B2FFF;">퇴근 전 체크리스트</div>
        <div class="checklist-items">
            ☐ &nbsp;벡터 DB 구축 및 검색 테스트 완료 &nbsp;&nbsp;&nbsp;&nbsp;
            ☐ &nbsp;RFP 업로드 → 요구사항 구조화 추출 동작 확인
        </div>
    </div>
</div>
</body></html>"""


# ═══════════════════════════════════════
# 슬라이드 5 — 수요일
# ═══════════════════════════════════════
wed = f"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8"><title>4/22 수요일</title>{common_style}
</head><body>
<div class="slide">
    <div class="header-row">
        <div class="badge" style="background:#FFA500;">WED</div>
        <div class="header-date">4/22 (수) &nbsp;오후 1시~6시</div>
    </div>
    <div class="title">제안서 생성 핵심 로직 개발</div>
    <div class="accent-line" style="background:#FFA500; width:120px; margin-bottom:16px;"></div>

    <div class="highlight-banner" style="background:#FFA500;">
        ⚡ &nbsp;이 날이 가장 중요하다. 5시간 전부를 집중해라.
    </div>

    <div class="three-col">
        <div class="card">
            <div class="card-time" style="color:#FFA500;">1:00 ~ 2:00</div>
            <div class="card-title">목차 자동 구성 로직</div>
            <ul class="card-list">
                <li>RFP 분석 결과 기반 목차 자동 생성</li>
                <li>RFP에 목차 지정 있으면 그것을 따름</li>
                <li>없으면 회사 공통 목차 구조를 기본값으로</li>
                <li>평가 배점 높은 항목에 더 많은 내용 할당</li>
            </ul>
        </div>
        <div class="card">
            <div class="card-time" style="color:#FFA500;">2:00 ~ 4:00</div>
            <div class="card-title">전체 파이프라인 구현</div>
            <ul class="card-list">
                <li>RFP 분석 → 벡터 DB 검색 → LLM 생성 연결</li>
                <li>섹션별로 나눠서 생성하는 구조</li>
                <li>각 섹션 생성 시 유사 과거 제안서 참고</li>
                <li>한 번에 전체 생성 ✕ → 섹션별 생성 ○</li>
            </ul>
        </div>
        <div class="card">
            <div class="card-time" style="color:#FFA500;">4:00 ~ 6:00</div>
            <div class="card-title">프롬프트 튜닝 ★</div>
            <ul class="card-list">
                <li>핵심 1: RFP 요구사항에 정확히 대응하는 내용</li>
                <li>핵심 2: 기존 제안서의 톤앤매너 유지</li>
                <li>같은 입력으로 프롬프트만 바꿔 최소 3회 비교</li>
                <li>버전별 차이와 품질을 기록으로 남겨라</li>
            </ul>
        </div>
    </div>

    <div class="checklist-bar">
        <div class="checklist-label" style="color:#FFA500;">퇴근 전 체크리스트</div>
        <div class="checklist-items">
            ☐ &nbsp;RFP 분석 → 목차 구성 → 섹션별 제안서 생성 전체 흐름 동작<br>
            ☐ &nbsp;생성 내용이 RFP 요구사항 반영 확인 &nbsp;&nbsp;&nbsp;&nbsp;
            ☐ &nbsp;프롬프트 버전별 비교 기록
        </div>
    </div>
</div>
</body></html>"""


# ═══════════════════════════════════════
# 슬라이드 6 — 목요일
# ═══════════════════════════════════════
thu = f"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8"><title>4/23 목요일</title>{common_style}
</head><body>
<div class="slide">
    <div class="header-row">
        <div class="badge" style="background:#FF6B9D;">THU</div>
        <div class="header-date">4/23 (목) &nbsp;오후 1시~6시</div>
    </div>
    <div class="title">UI 구현 및 파일 출력</div>
    <div class="accent-line" style="background:#FF6B9D; width:120px; margin-bottom:20px;"></div>

    <div class="two-col-wide-right">
        <div class="card" style="height:100%;">
            <div class="card-time" style="color:#FF6B9D;">1:00 ~ 3:00</div>
            <div class="card-title">웹 UI 구현 (Streamlit / Gradio)</div>
            <div class="sub-label" style="color:#FF6B9D; margin-top:8px;">화면 흐름</div>
            <div style="font-size:13px; color:#fff; line-height:2.2;">
                ❶ &nbsp;RFP 파일 업로드<br>
                ❷ &nbsp;RFP 분석 결과 확인 (검토 및 수정 가능)<br>
                ❸ &nbsp;제안서 생성 버튼<br>
                ❹ &nbsp;섹션별 생성 결과 확인<br>
                ❺ &nbsp;파일 다운로드
            </div>
        </div>
        <div style="display:flex; flex-direction:column; gap:16px;">
            <div class="card" style="flex:1;">
                <div class="card-time" style="color:#FF6B9D;">3:00 ~ 5:00</div>
                <div class="card-title">파일 출력 기능 개발</div>
                <ul class="card-list">
                    <li>python-docx (Word) 또는 python-pptx (PPT) 출력</li>
                    <li>기존 PPT 템플릿 활용 가능하면 최고</li>
                    <li>시간 부족 시 최소 Word 출력은 반드시 완성</li>
                </ul>
            </div>
            <div class="card" style="flex:1;">
                <div class="card-time" style="color:#FF6B9D;">5:00 ~ 6:00</div>
                <div class="card-title">전체 흐름 반복 테스트</div>
                <ul class="card-list">
                    <li>RFP 업로드 → 분석 → 생성 → 파일 다운로드 전체 테스트</li>
                    <li>깨지는 부분 수정 + 프롬프트 최종 튜닝</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="checklist-bar">
        <div class="checklist-label" style="color:#FF6B9D;">퇴근 전 체크리스트</div>
        <div class="checklist-items">
            ☐ &nbsp;RFP 업로드 → 분석 → 생성 → 파일 다운로드 전체 흐름 동작 &nbsp;&nbsp;&nbsp;&nbsp;
            ☐ &nbsp;출력 파일 정상 확인
        </div>
    </div>
</div>
</body></html>"""


# ═══════════════════════════════════════
# 슬라이드 7 — 금요일
# ═══════════════════════════════════════
fri = f"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8"><title>4/24 금요일</title>{common_style}
</head><body>
<div class="slide">
    <div class="header-row">
        <div class="badge" style="background:#00FF88; color:#1A1A2E;">FRI</div>
        <div class="header-date">4/24 (금) &nbsp;오후 1시~6시</div>
    </div>
    <div class="title">정리 및 최종 발표</div>
    <div class="accent-line" style="background:#00FF88; width:120px; margin-bottom:20px;"></div>

    <div class="two-col" style="margin-bottom:20px;">
        <div class="card">
            <div class="card-time" style="color:#00FF88;">1:00 ~ 2:30</div>
            <div class="card-title">코드 정리 + 문서화</div>
            <ul class="card-list">
                <li>코드 정리 및 README 작성</li>
                <li>설치/실행 방법, 폴더 구조, 기술 스택 정리</li>
                <li>발표 자료 준비</li>
            </ul>
        </div>
        <div class="card">
            <div class="card-time" style="color:#00FF88;">2:30 ~ 4:00</div>
            <div class="card-title">발표 리허설</div>
            <ul class="card-list">
                <li>데모가 실제로 동작하는지 최종 확인</li>
                <li>데모용 RFP 샘플 미리 준비</li>
                <li>발표 시간 체크 (30분 내외)</li>
            </ul>
        </div>
    </div>

    <div class="card">
        <div class="card-time" style="color:#00FF88;">4:00 ~ 6:00 &nbsp;최종 발표 및 라이브 데모</div>
        <div style="display:grid; grid-template-columns:auto 1fr; gap:8px 16px; margin-top:14px; align-items:center;">
            <div class="flow-num" style="color:#00FF88;">01</div><div class="flow-text">시스템 구조 — RFP 분석부터 제안서 출력까지의 전체 흐름</div>
            <div class="flow-num" style="color:#00FF88;">02</div><div class="flow-text">라이브 데모 — 실제 RFP를 넣어 제안서 생성 시연</div>
            <div class="flow-num" style="color:#00FF88;">03</div><div class="flow-text">RFP 분석 정확도 — 추출된 요구사항이 실제 RFP와 일치하는지</div>
            <div class="flow-num" style="color:#00FF88;">04</div><div class="flow-text">기존 제안서 vs AI 생성 제안서 비교</div>
            <div class="flow-num" style="color:#00FF88;">05</div><div class="flow-text">한계점과 개선 아이디어</div>
        </div>
    </div>
</div>
</body></html>"""


# ═══════════════════════════════════════
# 슬라이드 8 — 산출물 & 유의사항
# ═══════════════════════════════════════
final = f"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8"><title>산출물 및 유의사항</title>{common_style}
</head><body>
<div class="slide">
    <div class="accent-line" style="background:#00D2FF;"></div>
    <div class="title" style="margin-bottom:24px;">최종 산출물 & 유의사항</div>

    <div class="two-col" style="grid-template-columns:1fr 1fr; gap:28px;">
        <div class="card" style="height:100%;">
            <div class="sub-label" style="color:#00D2FF; font-size:16px; margin-bottom:16px;">최종 산출물 체크리스트</div>
            <div style="font-size:14px; line-height:2.4; color:#fff;">
                ☐ &nbsp;텍스트 추출 스크립트<br>
                ☐ &nbsp;벡터 DB 구축 코드<br>
                ☐ &nbsp;RFP 분석 모듈<br>
                ☐ &nbsp;제안서 생성 핵심 로직 + 프롬프트 템플릿<br>
                ☐ &nbsp;웹 UI (RFP 업로드 → 분석 → 생성 → 다운로드)<br>
                ☐ &nbsp;파일 출력 기능 (Word 또는 PPT)<br>
                ☐ &nbsp;README<br>
                ☐ &nbsp;발표 자료
            </div>
        </div>
        <div class="card" style="height:100%;">
            <div class="sub-label" style="color:#FFA500; font-size:16px; margin-bottom:16px;">유의사항</div>
            <div style="font-size:14px; color:#fff; font-weight:700; margin-bottom:14px;">총 작업 시간은 25시간이다.</div>
            <div style="font-size:13px; color:#B0B0C0; line-height:1.9; margin-bottom:16px;">
                완벽한 제안서를 만드는 것이 목표가 아니다.<br>
                RFP를 분석해서 요구사항을 정확히 파악하고,<br>
                그에 맞는 초안을 우리 회사 스타일로 빠르게<br>
                뽑아주는 도구를 만드는 것이 목표다.
            </div>
            <div style="font-size:13px; color:#B0B0C0; line-height:1.9; margin-bottom:16px;">
                사람이 검토하고 다듬는 것을 전제로 한<br>
                초안 생성 도구라는 점을 잊지 마라.
            </div>
            <div style="font-size:13px; color:#FFD93D; font-weight:700; margin-bottom:6px;">
                매일 퇴근 전 체크리스트를 반드시 달성해라.
            </div>
            <div style="font-size:13px; color:#B0B0C0; line-height:1.9;">
                하루라도 밀리면 금요일 발표에 영향이 간다.<br>
                막히면 혼자 끙끙대지 말고<br>
                GenSpark과 Cursor를 최대한 활용해라.
            </div>
        </div>
    </div>
</div>
</body></html>"""


# ═══════════════════════════════════════
# 파일 저장
# ═══════════════════════════════════════
slides = [
    ("01_표지.html", cover),
    ("02_전체흐름.html", flow),
    ("03_월요일_4월20일.html", mon),
    ("04_화요일_4월21일.html", tue),
    ("05_수요일_4월22일.html", wed),
    ("06_목요일_4월23일.html", thu),
    ("07_금요일_4월24일.html", fri),
    ("08_산출물_유의사항.html", final),
]

slide_nav_meta = [
    (None, "02_전체흐름.html", 1),
    ("01_표지.html", "03_월요일_4월20일.html", 2),
    ("02_전체흐름.html", "04_화요일_4월21일.html", 3),
    ("03_월요일_4월20일.html", "05_수요일_4월22일.html", 4),
    ("04_화요일_4월21일.html", "06_목요일_4월23일.html", 5),
    ("05_수요일_4월22일.html", "07_금요일_4월24일.html", 6),
    ("06_목요일_4월23일.html", "08_산출물_유의사항.html", 7),
    ("07_금요일_4월24일.html", None, 8),
]

for (filename, content), (prev_href, next_href, page_num) in zip(slides, slide_nav_meta):
    nav = nav_block(prev_href, next_href, page_num, current_filename=filename)
    content = content.replace("</body>", f"\n{nav}\n</body>")
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ 총 {len(slides)}개 HTML 파일 생성 완료")
print(f"📁 저장 위치: {os.path.abspath(output_dir)}/")
for filename, _ in slides:
    print(f"   - {filename}")
