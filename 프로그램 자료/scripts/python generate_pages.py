import os
from pathlib import Path

# 프로그램 자료 루트 (본 파일은 scripts/ 안에 있음)
PROG_ROOT = Path(__file__).resolve().parent.parent

# ── 공통 CSS ──────────────────────────────────────────────────
COMMON_CSS = """
  :root {
    --primary:#6c63ff;--secondary:#f50057;--dark:#1a1a2e;
    --card:#16213e;--card2:#0f3460;--text:#e0e0e0;--muted:#a0a0b0;
    --success:#00e676;--warning:#ffab00;--info:#40c4ff;--phase:#7c4dff;
  }
  *{margin:0;padding:0;box-sizing:border-box;}
  body{background:var(--dark);color:var(--text);font-family:'Segoe UI',sans-serif;line-height:1.7;}
  a{color:var(--primary);text-decoration:none;}
  .topnav{background:var(--card);padding:14px 32px;display:flex;align-items:center;gap:12px;border-bottom:2px solid var(--primary);}
  .topnav svg{width:28px;height:28px;}
  .breadcrumb{font-size:.9rem;color:var(--muted);}
  .breadcrumb span{color:var(--text);font-weight:600;}
  .hero{background:linear-gradient(135deg,var(--card2),var(--card));padding:48px 32px 36px;border-bottom:1px solid #ffffff18;}
  .hero .meta{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:16px;}
  .chip{padding:4px 14px;border-radius:20px;font-size:.78rem;font-weight:700;}
  .chip.week{background:#7c4dff33;color:#b39ddb;border:1px solid #7c4dff55;}
  .chip.day{background:#00e67622;color:#00e676;border:1px solid #00e67644;}
  .chip.date{background:#40c4ff22;color:#40c4ff;border:1px solid #40c4ff44;}
  .chip.phase{background:#f5005722;color:#f48fb1;border:1px solid #f5005744;}
  .hero h1{font-size:2rem;font-weight:800;margin-bottom:10px;}
  .hero h1 span{color:var(--primary);}
  .hero p{color:var(--muted);max-width:640px;}
  .container{max-width:960px;margin:0 auto;padding:40px 24px;}
  .section-title{font-size:1.2rem;font-weight:700;margin-bottom:20px;display:flex;align-items:center;gap:10px;}
  .section-title svg{width:22px;height:22px;}
  .timeline{position:relative;padding-left:28px;margin-bottom:40px;}
  .timeline::before{content:'';position:absolute;left:7px;top:0;bottom:0;width:2px;background:var(--primary);opacity:.35;}
  .tl-item{position:relative;margin-bottom:22px;}
  .tl-item::before{content:'';position:absolute;left:-24px;top:6px;width:12px;height:12px;border-radius:50%;background:var(--primary);box-shadow:0 0 8px var(--primary);}
  .tl-time{font-size:.78rem;color:var(--primary);font-weight:700;margin-bottom:2px;}
  .tl-title{font-weight:700;font-size:1rem;margin-bottom:4px;}
  .tl-desc{font-size:.88rem;color:var(--muted);}
  .cards-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:18px;margin-bottom:36px;}
  .card{background:var(--card);border:1px solid #ffffff15;border-radius:12px;padding:22px 20px;}
  .card h3{font-size:1rem;font-weight:700;margin-bottom:8px;}
  .card p{font-size:.85rem;color:var(--muted);}
  .card.blue{border-top:3px solid #40c4ff;}
  .card.purple{border-top:3px solid #7c4dff;}
  .card.green{border-top:3px solid #00e676;}
  .card.orange{border-top:3px solid #ffab00;}
  .card.red{border-top:3px solid #f50057;}
  .code-block{background:#0d0d1a;border:1px solid #ffffff18;border-radius:10px;padding:20px;margin-bottom:28px;overflow-x:auto;}
  .code-block pre{font-family:'Courier New',monospace;font-size:.82rem;color:#a8d8a8;line-height:1.8;}
  .code-header{display:flex;align-items:center;gap:8px;margin-bottom:12px;}
  .lang-badge{background:var(--primary);color:#fff;font-size:.72rem;font-weight:700;padding:2px 10px;border-radius:10px;}
  .code-title{font-size:.88rem;color:var(--muted);}
  .tip-box{background:#7c4dff15;border:1px solid #7c4dff44;border-radius:10px;padding:18px 20px;margin-bottom:28px;display:flex;gap:12px;align-items:flex-start;}
  .tip-box svg{width:22px;height:22px;flex-shrink:0;margin-top:2px;}
  .tip-box p{font-size:.88rem;color:var(--muted);}
  .tip-box strong{color:var(--text);}
  .checklist{background:var(--card);border-radius:12px;padding:24px;margin-bottom:28px;}
  .checklist ul{list-style:none;}
  .checklist li{padding:8px 0;border-bottom:1px solid #ffffff0d;display:flex;align-items:flex-start;gap:10px;font-size:.9rem;}
  .checklist li:last-child{border-bottom:none;}
  .check-icon{width:20px;height:20px;flex-shrink:0;margin-top:1px;}
  .output-box{background:var(--card2);border:1px solid #40c4ff33;border-radius:12px;padding:24px;margin-bottom:40px;}
  .output-box h3{font-size:1rem;font-weight:700;color:#40c4ff;margin-bottom:14px;display:flex;align-items:center;gap:8px;}
  .output-box ul{list-style:none;}
  .output-box li{padding:6px 0;font-size:.88rem;display:flex;align-items:center;gap:8px;color:var(--muted);}
  .output-box li::before{content:'→';color:#40c4ff;font-weight:700;}
  .day-nav{display:flex;justify-content:space-between;align-items:center;padding:18px 0;border-top:1px solid #ffffff18;margin-top:10px;gap:8px;flex-wrap:wrap;}
  .day-nav-mid{display:flex;gap:10px;flex-wrap:wrap;align-items:center;justify-content:center;}
  .day-nav a{display:flex;align-items:center;gap:8px;padding:10px 20px;border-radius:8px;background:var(--card);font-weight:600;font-size:.9rem;transition:.2s;}
  .day-nav a:hover{background:var(--card2);}
  .styled-table{width:100%;border-collapse:collapse;margin-bottom:28px;font-size:.88rem;}
  .styled-table th{background:var(--card2);color:var(--primary);padding:10px 14px;text-align:left;font-weight:700;}
  .styled-table td{padding:10px 14px;border-bottom:1px solid #ffffff0d;color:var(--muted);}
  .styled-table tr:hover td{background:#ffffff05;}
  .kpt-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:36px;}
  .kpt-card{background:var(--card);border-radius:12px;padding:22px;}
  .kpt-card.keep{border-top:3px solid #00e676;}
  .kpt-card.problem{border-top:3px solid #f50057;}
  .kpt-card.try{border-top:3px solid #40c4ff;}
  .kpt-card h3{font-size:.95rem;font-weight:800;margin-bottom:12px;display:flex;align-items:center;gap:8px;}
  .kpt-card ul{list-style:none;}
  .kpt-card li{font-size:.83rem;color:var(--muted);padding:5px 0;border-bottom:1px solid #ffffff08;}
  .kpt-card li:last-child{border-bottom:none;}
  .kpt-card li::before{content:'• ';color:var(--primary);}
  .next-week{background:linear-gradient(135deg,#0f3460,#1a1a2e);border:1px solid var(--primary);border-radius:12px;padding:24px;margin-bottom:28px;}
  .next-week h3{font-size:1rem;font-weight:700;color:var(--primary);margin-bottom:16px;}
  .next-week-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;}
  .nw-day{background:var(--card);border-radius:8px;padding:12px 8px;text-align:center;}
  .nw-day .day-num{font-size:.75rem;color:var(--muted);margin-bottom:4px;}
  .nw-day .day-title{font-size:.78rem;font-weight:700;color:var(--text);}
  .prompt-box{background:#0d0d1a;border:1px solid #7c4dff55;border-radius:10px;padding:20px;margin-bottom:28px;}
  .prompt-box .pb-header{font-size:.8rem;color:#7c4dff;font-weight:700;margin-bottom:10px;}
  .prompt-box pre{font-family:'Courier New',monospace;font-size:.82rem;color:#e0e0e0;line-height:1.8;white-space:pre-wrap;}
  .pipeline{display:flex;gap:0;flex-wrap:wrap;margin-bottom:40px;align-items:stretch;}
  .pipe-step{flex:1;min-width:130px;background:var(--card);border:1px solid #ffffff18;padding:18px 12px;position:relative;text-align:center;}
  .pipe-step:not(:last-child)::after{content:'▶';position:absolute;right:-12px;top:50%;transform:translateY(-50%);color:var(--primary);font-size:1rem;z-index:2;}
  .pipe-step .pipe-label{font-weight:700;font-size:.88rem;margin-bottom:6px;}
  .pipe-step .pipe-desc{font-size:.76rem;color:var(--muted);}
  .pipe-step.s1{border-top:3px solid #40c4ff;}
  .pipe-step.s2{border-top:3px solid #7c4dff;}
  .pipe-step.s3{border-top:3px solid #00e676;}
  .pipe-step.s4{border-top:3px solid #ffab00;}
  .pipe-step.s5{border-top:3px solid #f50057;}
  @media(max-width:640px){.day-nav{flex-direction:column;}.day-nav-mid{order:-1;width:100%;}}
  @media(max-width:600px){.kpt-grid{grid-template-columns:1fr;}.next-week-grid{grid-template-columns:repeat(3,1fr);}.pipeline{flex-direction:column;}.pipe-step:not(:last-child)::after{content:'▼';right:50%;top:auto;bottom:-14px;}}
"""

# ── 공통 SVG ──────────────────────────────────────────────────
HOME_SVG  = '<svg viewBox="0 0 24 24" fill="none" stroke="#6c63ff" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'
CLOCK_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="#6c63ff" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'
CHECK_SVG = '<svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="#00e676" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>'
OUT_SVG   = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#40c4ff" stroke-width="2"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>'
PREV_SVG  = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg>'
NEXT_SVG  = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>'
TIP_SVG   = '<svg viewBox="0 0 24 24" fill="none" stroke="#7c4dff" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>'
GRID_SVG  = '<svg viewBox="0 0 24 24" fill="none" stroke="#6c63ff" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>'
EDIT_SVG  = '<svg viewBox="0 0 24 24" fill="none" stroke="#6c63ff" stroke-width="2"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg>'

from timelines import TIMELINES

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

# ══════════════════════════════════════════════════════════════
# 전체 페이지 데이터 — 근거: 「AI 업무 경험 프로그램 계획서」최종 (미래내일 일경험·인턴형, 아이뱅크, 2026.4.13)
# 멘토 조준형 · 인턴 개별 수행 · 기간 2026.04.13~06.05(8주) · 인턴 업무시간: 평일 13:00–18:00(5h/일) · 주 25시간 · 오프라인 중심
# 멘토링: 주간 멘토 미팅 30분 + 개인 데일리 체크인 15분 (전날/오늘/막힘) (계획서 §5)
# 미니 프로젝트 후보(4주차 확정): VOC·리뷰 대시보드 / RAG 챗봇 / AI 트렌드 브리핑 / 업무 자동화 플랫폼 (계획서 §4)
# 일일 타임블록: 13:00–18:00 (5구간 × 1시간) — 평일 고정
# ══════════════════════════════════════════════════════════════
PAGES = [

  # ────────────────── WEEK 1 (계획서: 온보딩·AI 트렌드 오리엔테이션·환경 셋업·LLM 동향 과제) ──────────────────
  (1, 1, "2026-04-13 (월)", "온보딩 & AI 트렌드 오리엔테이션",
   "계획서 1주차: 회사·부서 업무 파악, 인턴 업무 목표·계획 공유(OT 연계), 프로그램·AI 트렌드 학습 목표를 정합니다.",
   "Phase 1 – 탐색·환경 구축 (1~2주)",
   TIMELINES[(1, 1)],
   [("blue","📋 계획서 핵심","AI 트렌드 이해 + Claude·Cursor·젠스파크·오픈클로 실무 + 미니 프로젝트·포트폴리오"),
    ("purple","👥 OT 연계","부서 목표와 인턴 목표를 한 페이지에 맞추기"),
    ("green","🤖 LLM 동향","계획서 과제 방향: 최신 모델별 강점·업무 적합성"),
    ("orange","📝 일지","주간 미팅 전까지 매일 기록해 멘토링 효율 극대화")],
   ["프로그램·8주 일정 이해","부서 업무·소통 방식 메모",
    "인턴 개인 목표·계획 문서 초안","LLM 개요 표 1페이지",
    "일지 양식 파일 생성","내일 환경 셋업 목록 작성"],
   ["goal_plan_w1d1.md — 인턴 목표·계획(OT 연계)","llm_overview_w1.md — 모델군 한 페이지 요약","journal_template.md — 주간 일지 템플릿"],
   "계획서에 따라 <strong>멘토와 주간 30분 미팅</strong>에서 목표·진도·협의 사항을 맞춥니다. 첫 주는 '무엇을 배울지'보다 '왜 배우는지'가 문서와 일치하는지가 중요합니다.",
   sample_extra_html(1, 1)),

  (1, 2, "2026-04-14 (화)", "AI 개발 환경 셋업 ① — Claude Cowork & Cursor",
   "계획서 1주차: AI 개발 환경 셋업 — Claude Cowork, Cursor IDE 설치·계정·기본 동작 확인.",
   "Phase 1 – 탐색·환경 구축 (1~2주)",
   TIMELINES[(1, 2)],
   [("blue","Claude Cowork","계획서: 주간 업무 정리·리서치 보고서 초안·텍스트 분석 지원"),
    ("purple","Cursor IDE","계획서: Python 완성·리팩터링·API 연동 실습 예정"),
    ("green","역할 정리","문서·코드·분석 — 본인 산출물 기준으로 Cowork/Cursor 쓰임새·폴더 규칙 통일"),
    ("orange","보안","API 키·내부 자료는 공유 전 항상 검토")],
   ["Claude Cowork 실행·첫 대화 성공","Cursor 설치 및 Tab 동작 확인",
    "개인 작업 규칙(Cowork/Cursor·폴더) 1페이지","API 키 관리 규칙(코드 미삽입) 확인",
    "일지에 이슈·질문 기록","멘토 미팅용 질문 3개 우선순위"],
   ["cowork_first_session.md","cursor_setup_notes.md","open_questions_w1.md"],
   "계획서의 툴 매트릭스에 따르면 Cowork는 <strong>파일·리포트</strong>에, Cursor는 <strong>코드·API</strong>에 초점을 둡니다. 첫 주에 습관을 나누면 이후 주차가 수월합니다.",
   sample_extra_html(1, 2)),

  (1, 3, "2026-04-15 (수)", "AI 개발 환경 셋업 ② — 젠스파크 & 오픈클로",
   "계획서 1주차: 젠스파크(Genspark)·오픈클로 설치·계정 생성 및 첫 워크플로우.",
   "Phase 1 – 탐색·환경 구축 (1~2주)",
   TIMELINES[(1, 3)],
   [("blue","젠스파크","계획서: 정책·글로벌 사례 리서치, 멀티소스 종합"),
    ("purple","오픈클로","계획서: 반복 리포트·템플릿 자동화"),
    ("green","파이프라인 감각","수집(Genspark) → 분석(Cowork) → 배포(오픈클로)"),
    ("orange","다음 주 예고","공공·행정 분야 AI 도입 사례 심화 리서치")],
   ["젠스파크 Sparkpage 1개 이상","오픈클로 테스트 플로우 1개 성공",
    "Genspark→Cowork 연동 메모","4툴 체크리스트 완성",
    "검색 키워드 5개 목록","2주차 심화 리서치 질문 초안 1개"],
   ["genspark_sparkpage_w1.md","openclaro_first_workflow.png","tool_checklist_w1.md"],
   "계획서에서 젠스파크는 <strong>검색·Sparkpage</strong>, 오픈클로는 <strong>반복 자동화</strong>에 각각 특화되어 있습니다. 한 번의 시나리오로 두 툴을 연결해 보는 것이 핵심입니다.",
   sample_extra_html(1, 3)),

  (1, 4, "2026-04-16 (목)", "최신 LLM 동향 과제 (GPT-4o·Claude·Gemini)",
   "계획서 1주차 핵심 과제: 최신 LLM 동향(GPT-4o, Claude 3.7 전후, Gemini 2.0 등) 조사·정리.",
   "Phase 1 – 탐색·환경 구축 (1~2주)",
   TIMELINES[(1, 4)],
   [("blue","GPT-4o","OpenAI 측 최신 제품군·엔터프라이즈 기능"),
    ("purple","Claude 3.x","Anthropic — 긴 문맥·분석·코드"),
    ("green","Gemini 2.x","Google — 검색·워크스페이스 연계"),
    ("orange","공공·정책 맥락","계획서: 공공·행정 분야 활용 사례 파악이 목표 목록에 포함")],
   ["3모델군 비교표 초안","Genspark Sparkpage 2개",
    "Cowork 요약·편집 완료","과제 문서 v0.9 저장",
    "차주 API 실습을 위한 참고 링크","과제 문서 내 [TODO] 보강 포인트 목록"],
   ["llm_trend_assignment_w1.pdf 또는 .md","model_compare_table_w1.md","sparkpage_refs_w1/"],
   "계획서의 <strong>목표(세부 내용)</strong>에는 최신 LLM·생성형 AI 동향과 공공·행정 분야 활용 사례 파악이 명시되어 있습니다. 숫자·출처가 있는 문장일수록 보고서 가치가 높아집니다.",
   sample_extra_html(1, 4)),

  (1, 5, "2026-04-17 (금)", "주간 미팅(30분) & 일지·1주차 산출물",
   "계획서 1주차: 멘토와 주간 미팅으로 일정·협의 사항 정렬, 일지 양식 확정, 핵심 산출물 패키징.",
   "Phase 1 – 탐색·환경 구축 (1~2주)",
   TIMELINES[(1, 5)],
  [("blue","✅ Keep","4툴 설치·첫 시나리오, LLM 과제 착수"),
    ("red","⚠️ Problem","환경 이슈·시간 배분 — 구체적으로 기록"),
    ("green","🚀 Try","2주차: 공공·행정 사례·워크플로우·프롬프트 기초"),
    ("orange","📌 계획서 메모","상황에 따라 멘토 재량으로 조정 가능")],
   ["주간 미팅 완료","피드백 문서화",
    "1주차 KPT 완성","핵심 산출물 폴더 제출(또는 공유 링크)",
    "일지 5일치 백업","2주차 검색 키워드 확정"],
   ["weekly_summary_w1.md","retrospective_w1.md","feedback_w1.md","deliverables_w1/"],
   "계획서 말미: <strong>주간 미팅으로 진도와 방향을 수시로 점검</strong>하며, 인턴에게 가장 의미 있는 경험이 되도록 하는 것이 핵심 목표입니다. 피드백은 다음 주 작업 순서로 바로 연결하세요.",
   sample_extra_html(1, 5)),

  # ────────────────── WEEK 2 (계획서: 트렌드 심화·공공·행정 사례·워크플로우·프롬프트·보고서 초안) ──────────────────
  (2, 1, "2026-04-20 (월)", "AI 트렌드 심화 리서치 & 툴 실습",
   "계획서 2주차: AI 트렌드 심화 리서치와 첫 툴 실습 — 전주 과제를 바탕으로 심화 키워드·범위를 정합니다.",
   "Phase 1 – 탐색·환경 구축 (1~2주)",
   TIMELINES[(2, 1)],
   [("blue","계획서 2주차","AI 트렌드 심화 리서치 + 첫 AI 툴 실습"),
    ("purple","심화","전주 대비 키워드·근거 깊이를 한 단계 올리기"),
    ("green","산출물","Sparkpage·요약 md 누적"),
    ("orange","다음","공공·행정 사례 집중 리서치")],
   ["심화 키워드 5개 확정","Genspark Sparkpage 2개 이상",
    "Claude 요약 1건","내일 검색 질문 5개",
    "일지 기록"],
   ["deep_dive_w2d1.md","sparkpage_w2d1/","exec_bullets_w2d1.md"],
   "계획서 2주차는 <strong>심화 리서치와 툴 실습</strong>이 같은 줄에 묶여 있습니다. 읽기만 하지 말고, 반드시 툴로 '만든 결과물'을 남기세요.",
   sample_extra_html(2, 1)),

  (2, 2, "2026-04-21 (화)", "젠스파크 — 국내외 산업별 AI 도입 사례",
   "계획서 2주차(권미정): 젠스파크로 국내외 산업별 AI 도입 사례를 조사합니다. (챗봇·자동화·AI Agent·서비스 운영 등 — 계획서 §3주차 2주차 항목)",
   "Phase 1 – 탐색·환경 구축 (1~2주)",
   TIMELINES[(2, 2)],
   [("blue","챗봇·안내","민원·CS·내부 헬프데스크"),
    ("purple","문서·지식","요약·분류·RAG"),
    ("green","데이터·분석","대시보드·질의응답"),
    ("orange","근거","공개 보도·공식 자료 인용")],
   ["유형별 사례 3개 이상","Sparkpage 2개 이상",
    "비교 표 완성","Cowork 인사이트 문단",
    "출처 목록"],
   ["industry_ai_cases_w2.md","sparkpage_cases_kr.md","sparkpage_cases_intl.md"],
   "4주차에 확정할 <strong>개인 미니 프로젝트 후보(§4)</strong>와 연결해 사례를 모으세요. 출처·시점을 적어 신뢰도를 확보하는 것이 핵심입니다.",
   sample_extra_html(2, 2)),

  (2, 3, "2026-04-22 (수)", "Claude Cowork — 정리·요약 워크플로우",
   "계획서 2주차: Claude Cowork로 수집 내용을 정리·요약하는 워크플로우 실습.",
   "Phase 1 – 탐색·환경 구축 (1~2주)",
   TIMELINES[(2, 3)],
   [("blue","Cowork","계획서: 파일 관리·리포트 초안에 강점"),
    ("purple","워크플로우","입력→요약→검증→저장"),
    ("green","품질","한계·리스크 문장 포함"),
    ("orange","연계","내일 ChatGPT/프롬프트 기초와 연결")],
   ["요약 템플릿 1개","요약 프롬프트 2종",
    "정제된 리포트 v0.1","체크리스트 완료",
    "일지","주간 미팅 전 일지·산출물 폴더 정리"],
   ["cowork_summary_workflow.md","public_sector_report_v0.1.md"],
   "계획서는 Cowork를 <strong>정리·요약 워크플로우</strong>의 중심에 둡니다. 한 번에 완벽한 답을 요구하기보다, 대화로 다듬는 과정을 남기세요.",
   sample_extra_html(2, 3)),

  (2, 4, "2026-04-23 (목)", "ChatGPT / 프롬프트 엔지니어링 기초",
   "계획서 2주차: ChatGPT 등 대화형 LLM과 프롬프트 엔지니어링 기초 — 역할 지정, Chain-of-Thought.",
   "Phase 1 – 탐색·환경 구축 (1~2주)",
   TIMELINES[(2, 4)],
   [("blue","역할","Role이 톤·전문용어를 바꿈"),
    ("purple","CoT","단계가 보일수록 검증 가능"),
    ("green","Format","보고서·API 연동에 유리"),
    ("orange","비교","툴별 강점 파악")],
   ["역할 프롬프트 비교 실험","CoT 예시 1건",
    "프롬프트 카드 5장","ChatGPT vs Claude 메모",
    "내일 오픈클로 보고서 초안에 쓸 프롬프트 초안","보고서 목차·섹션별 입력 목록"],
   ["prompt_cards_w2.md","cot_example_w2.md"],
   "계획서에 <strong>역할 지정·연쇄 추론(Chain-of-Thought)</strong>가 명시되어 있습니다. 공공·정책 도메인 용어를 포함한 역할 프롬프트를 직접 써 보세요.",
   sample_extra_html(2, 4)),

  (2, 5, "2026-04-24 (금)", "오픈클로 보고서 초안 & 멘토 피드백 (1차 완성)",
   "계획서 2주차: 오픈클로로 보고서 초안 생성·편집, 1차 완성 및 멘토 피드백 — 핵심 산출물(약 10페이지 분량 목표).",
   "Phase 1 – 탐색·환경 구축 (1~2주)",
   TIMELINES[(2, 5)],
   [("blue","산출물","계획서: 트렌드·사례·워크플로우·프롬프트를 아우르는 통합 보고서"),
    ("purple","분량","약 10페이지 목표(조정 가능)"),
    ("green","피드백","멘토·계획서 모두 유연 조정 원칙"),
    ("orange","다음 주","코딩 실습·API·문서화")],
   ["보고서 1차 완성(PDF)","멘토 피드백 반영 목록",
    "feedback_w2.md","retrospective_w2.md",
    "3주차 환경 점검(venv·API 키)"],
   ["ai_trend_report_round1.pdf","feedback_w2.md","retrospective_w2.md"],
   "계획서 2주차 핵심 산출물은 <strong>보고서 초안 + 멘토 피드백</strong>입니다. 완벽함보다 '근거·구조·다음 액션'이 보이는지가 중요합니다.",
   sample_extra_html(2, 5)),

  # ────────────────── WEEK 3 (계획서: Cursor+Python 코딩·API·Few-shot/CoT·문서화) ──────────────────
  (3, 1, "2026-04-27 (월)", "Cursor + Python AI 코딩 실습",
   "계획서 3주차: Cursor IDE를 활용한 AI 코딩 실습 — 계획서상 '코딩 어시스트 IDE·Python 완성·리팩터링·디버깅'에 해당합니다.",
   "Phase 2 – AI 툴 심화·개인 역량 (3~5주)",
   TIMELINES[(3, 1)],
   [("blue","Cursor","계획서 툴 매트릭스: API 연동 실습·코드 품질"),
    ("purple","Python","스크립트 자동화의 기본 단위"),
    ("green","습관","작은 커밋·짧은 함수"),
    ("orange","다음","데이터 분석 작성·GA4 연계")],
   ["venv·실행 성공","리팩터 1회",
    "치트시트 1페이지","일지","첫 파이프라인 실행 스크린샷 또는 로그"],
   ["cursor_shortcuts_w3.md","src/hello_pipeline.py"],
   "계획서 3주차는 <strong>Cursor로 코딩하는 실제 리듬</strong>을 만드는 주입니다. 툴 설명보다 '실행한 코드'가 산출물이 됩니다.",
   sample_extra_html(3, 1)),

  (3, 2, "2026-04-28 (화)", "데이터 분석 작성 & GA4 등 경험 자동화",
   "계획서 3주차: IDE를 활용한 데이터 분석 작성 — 기존 GA4·SQL·대시보드 경험을 AI로 자동화하는 스크립트에 도전합니다.",
   "Phase 2 – AI 툴 심화·개인 역량 (3~5주)",
   TIMELINES[(3, 2)],
   [("blue","GA4","계획서: 인턴 역량 표에 GA4·퍼널 등 기재"),
    ("purple","자동화","매주 같은 리포트를 스크립트로"),
    ("green","재현성","입력 바꾸면 출력만 갱신"),
    ("orange","공공·정책 맥락","정책 뉴스·공공데이터 텍스트로 확장 예고(5주차)")],
   ["집계 노트북 또는 .py","auto_report_weekly_skeleton.py",
    "한 장 요약 md","자동화 스크립트 실행·오류 메모"],
   ["data_analysis_w3d2.ipynb","auto_report_weekly_skeleton.py"],
   "계획서는 <strong>기존 데이터 분석 경험을 AI와 결합</strong>하는 것을 명시합니다. 익숙한 지표 하나를 스크립트로 옮기는 것이 첫 단계입니다.",
   sample_extra_html(3, 2)),

  (3, 3, "2026-04-29 (수)", "OpenAI / Claude API — 분류·요약 파이프라인",
   "계획서 3주차: OpenAI API·Claude API 호출 — 간단 텍스트 분류·요약 파이프라인 구현.",
   "Phase 2 – AI 툴 심화·개인 역량 (3~5주)",
   TIMELINES[(3, 3)],
   [("blue","OpenAI","Chat Completions 패턴"),
    ("purple","Claude","messages.create 패턴"),
    ("green","파이프라인","입력 JSON → 출력 JSON"),
    ("orange","보안","키·PII 분리")],
   ["분류·요약 스크립트 각 1개","샘플 입출력 JSON",
    "api_usage_notes.md","샘플 요청·응답 JSON 검증"],
   ["api_classify.py","api_summarize.py","api_usage_notes.md"],
   "계획서의 <strong>간단 분류·요약 파이프라인</strong>은 이후 미니 프로젝트의 핵심 부품이 됩니다. 에러 처리까지 넣어 '실제에 가까운' 형태로 만드세요.",
   sample_extra_html(3, 3)),

  (3, 4, "2026-04-30 (목)", "프롬프트 심화 — Few-shot & Chain-of-Thought",
   "계획서 3주차: 프롬프트 엔지니어링 심화 — Few-shot, Chain-of-Thought를 코드·실험으로 연결합니다.",
   "Phase 2 – AI 툴 심화·개인 역량 (3~5주)",
   TIMELINES[(3, 4)],
   [("blue","Few-shot","예시 품질이 성능을 좌우"),
    ("purple","CoT","설명 가능한 AI"),
    ("green","측정","숫자로 비교"),
    ("orange","다음","문서화·README")],
   ["비교 실험 완료","prompt_library_v2.md",
    "accuracy_comparison.md","실험 조건·재현 커맨드 한 줄"],
   ["prompt_experiment_w3.md","prompt_library_v2.md","accuracy_comparison.md"],
   "계획서에 명시된 <strong>Few-shot·Chain-of-Thought</strong>는 '프롬프트'가 아니라 '실험 결과'로 남길 때 학습이 완성됩니다.",
   sample_extra_html(3, 4)),

  (3, 5, "2026-05-01 (금)", "Cursor 단축키·완성 방법 문서화 & 3주차 회고",
   "계획서 3주차 핵심 산출물: LLM 연동 스크립트 + 가이드 — docstring·README·멘토 미팅·KPT.",
   "Phase 2 – AI 툴 심화·개인 역량 (3~5주)",
   TIMELINES[(3, 5)],
   [("blue","산출물","계획서: LLM 연동 스크립트 + 가이드"),
    ("purple","문서화","단축키·실행 방법·한계"),
    ("green","피드백","멘토·계획서 유연 조정"),
    ("orange","4주차","자동화·비교·미니 프로젝트 주제 준비")],
   ["README.md","README_llm_pipeline.md",
    "feedback_w3.md","retrospective_w3.md",
    "Git 커밋","README·가이드와 커밋 해시 기록"],
   ["README.md","llm_pipeline_guide.md","retrospective_w3.md"],
   "계획서 3주차는 <strong>스크립트와 가이드가 세트</strong>입니다. 멘토·검토자가 따라 해 보며 같은 결과가 나오게 쓰는 것이 목표입니다.",
   sample_extra_html(3, 5)),

  # ────────────────── WEEK 4 (계획서: Cowork 업무 자동화·파일/리포트 WF·반복 리포트·오픈클로 템플릿·툴 비교·미니 프로젝트 주제 확정) ──────────────────
  (4, 1, "2026-05-04 (월)", "Claude Cowork — AI 업무 자동화 실습",
   "계획서 4주차: Claude Cowork AI 업무 자동화 실습 — 파일 관리·정보 보고서 생성 워크플로우의 기초를 잡습니다.",
   "Phase 2 – AI 툴 심화·개인 역량 (3~5주)",
   TIMELINES[(4, 1)],
   [("blue","계획서","Cowork — 파일·리포트에 강점"),
    ("purple","자동화","반복 서술을 대화로 줄이기"),
    ("green","컴플라이언스","PII·내부명칭 주의"),
    ("orange","연계","내일 반복 리포트 자동화")],
   ["역할 프롬프트 1개","파일 업로드 분석 2회 이상",
    "1페이지 브리핑 1건","문서화 완료"],
   ["cowork_automation_w4.md","sample_briefing_w4.md"],
   "계획서 4주차는 <strong>Claude Cowork로 업무 자동화</strong>를 명시합니다. '분석'을 한 번에 끝내지 말고, 대화로 다듬는 흐름을 기록하세요.",
   sample_extra_html(4, 1)),

  (4, 2, "2026-05-05 (화)", "반복 업무 자동화 — 주간 리포트 초안",
   "계획서 4주차: 심화 활용(파일 관리·정보 보고서 생성 워크플로우)·반복 데이터(주간 리포트 초안) 자동화.",
   "Phase 2 – AI 툴 심화·개인 역량 (3~5주)",
   TIMELINES[(4, 2)],
   [("blue","📊 데이터 정제","pandas + Python으로 중복 제거, 형식 통일, 이상값 처리 자동화"),
    ("purple","📋 보고서 자동화","오픈클로 스케줄 트리거 → Claude 요약 → Markdown 저장 → 이메일 전송"),
    ("green","✉️ 이메일 초안","'수신자, 목적, 핵심 내용'만 입력하면 Claude가 전문적인 이메일 초안 생성"),
    ("orange","⏱ ROI 측정","자동화 전 수동 소요 시간 vs 자동화 후 시간 → 주간 절감 시간 계산")],
   ["반복 업무 5개 이상 목록화 및 우선순위 결정","CSV 자동 정제 파이프라인 작동 확인",
    "주간 보고서 자동 생성 워크플로우 완성","이메일 초안 자동화 코드 작성",
    "자동화 ROI 측정 완료 (시간 절감 정량화)","자동화 가이드 문서 작성"],
   ["auto_clean.py — CSV 자동 정제 코드","auto_report.py — 보고서 자동 생성 코드","email_draft.py — 이메일 초안 자동화 코드","automation_roi.md — 자동화 ROI 측정 결과"],
   "자동화 업무를 선정할 때 <strong>빈도 × 소요시간</strong>이 큰 것부터 시작하세요. 매일 30분씩 하는 작업을 자동화하면 주당 2.5시간, 연간 130시간을 절약할 수 있습니다. ROI를 수치로 보여주면 자동화의 가치가 명확해집니다.",
   sample_extra_html(4, 2)),

  (4, 3, "2026-05-06 (수)", "오픈클로 템플릿·워크플로우 설계",
   "계획서 4주차: 오픈클로로 반복 산출물(브리핑·회의록·리서치)을 템플릿화하고, 트리거·입력·출력을 문서로 고정합니다.",
   "Phase 2 – AI 툴 심화·개인 역량 (3~5주)",
   TIMELINES[(4, 3)],
   [("blue","📰 뉴스 브리핑","매일 09:00 트리거 → RSS/Genspark → Claude 3줄 요약 → 이메일 발송"),
    ("purple","📝 회의록 요약","텍스트 입력 → 의제별 분류 → 결정사항 + 액션 아이템 구조화"),
    ("green","🔍 리서치 자동화","키워드 → Genspark Sparkpage → Claude 인사이트 → Markdown 보고서"),
    ("orange","📐 설계 원칙","각 단계는 독립적으로 테스트 가능해야 하며 에러 처리가 포함되어야 함")],
   ["워크플로우 설계 원칙 5단계 숙지","AI 뉴스 브리핑 워크플로우 완성 및 테스트",
    "회의록 자동 요약 워크플로우 완성","리서치 보고서 워크플로우 완성",
    "3개 워크플로우 문서화 완료","멘토와 워크플로우 공유(또는 제출)"],
   ["workflow_news.md — 뉴스 브리핑 워크플로우","workflow_meeting.md — 회의록 요약 워크플로우","workflow_research.md — 리서치 보고서 워크플로우"],
   "오픈클로 워크플로우를 설계할 때 <strong>'이 워크플로우가 실패하면 어떻게 되는가?'</strong>를 항상 생각하세요. 각 단계에 에러 핸들링과 로그 저장을 추가하면 문제 발생 시 원인을 빠르게 파악할 수 있습니다.",
   sample_extra_html(4, 3)),

  (4, 4, "2026-05-07 (목)", "ChatGPT vs Claude 중심 AI 툴 비교",
   "계획서 4주차: 동일 과제로 ChatGPT·Claude(및 필요 시 Cursor·Genspark·오픈클로)를 비교하고, 업무 유형별 추천 규칙을 한 장으로 남깁니다.",
   "Phase 2 – AI 툴 심화·개인 역량 (3~5주)",
   TIMELINES[(4, 4)],
   [("blue","ChatGPT","범용·빠른 초안"),
    ("purple","Claude","긴 맥락·문서·분석"),
    ("green","공정 비교","입력·온도·모델명 기록"),
    ("orange","실무 규칙","언제 무엇을 쓸지 한 줄")],
   ["동일 입력 실험 2회 이상","비교 표 완성",
    "업무별 추천 가이드 1페이지","한계·주의 문구"],
   ["tool_comparison_matrix.md","tool_guide.md","comparison_note_w4.md"],
   "계획서 취지에 맞게 <strong>ChatGPT와 Claude를 반드시 같은 조건</strong>에서 겨루세요. '더 좋다'가 아니라 '이 업무에는 이유로 이쪽'이 보이게 쓰는 것이 목표입니다.",
   sample_extra_html(4, 4)),

  (4, 5, "2026-05-08 (금)", "중간점검·미니 PJ 주제 확정 & 4주차 회고",
   "계획서 4주차 금요일: §5.2 중간점검(1~3주 학습·실습 정리 발표) 후 §4 후보 중 개인 미니 프로젝트 주제 최종 확정, 산출물·일정 정리.",
   "Phase 2 – AI 툴 심화·개인 역량 (3~5주)",
   TIMELINES[(4, 5)],
   [("blue","협의","범위가 작을수록 완주"),
    ("purple","산출물","주차별 파일 이름 확정"),
    ("green","회고","측정 가능한 Try"),
    ("orange","5주차","데이터·파이프라인·Looker")],
   ["미니 PJ 개인 주제 확정","retrospective_w4.md",
    "handoff_w4_to_w5.md","repo 초기 구조"],
   ["meeting_notes_w4.md","retrospective_w4.md","handoff_w4_to_w5.md"],
   "미니 프로젝트는 <strong>완성도보다 학습·재현 가능한 산출물</strong>이 우선입니다. 멘토와 합의한 '이번 주 금요일까지의 정의'를 문장으로 남기세요.",
   sample_extra_html(4, 5)),

  # ────────────────── WEEK 5 (계획서: AI 데이터 분석·텍스트 파이프라인·Looker·글로벌 벤치마크 리서치·미니 PJ 기획서) ──────────────────
  (5, 1, "2026-05-11 (월)", "AI 기반 데이터 분석 — 인사이트 도출 착수",
   "계획서 5주차: AI 기반 데이터 분석 및 인사이트 도출 — 미니 프로젝트 주제와 연결된 분석 질문을 고정합니다.",
   "Phase 2 – AI 툴 심화·개인 역량 (3~5주)",
   TIMELINES[(5, 1)],
   [("blue","계획서","Python+AI 툴 결합 인사이트"),
    ("purple","역량 연계","텍스트마이닝·GA 등 기존 경험"),
    ("green","규제","개인·민감 행정 데이터 취급 주의"),
    ("orange","산출물","이후 파이프라인·기획서로 연결")],
   ["분석 질문 1문장","데이터 소스 표",
    "성공 지표 2개","미니 프로젝트 범위 초안"],
   ["mini_project_scope.md","data_sources_w5.md"],
   "계획서 5주차는 <strong>인사이트 도출</strong>이 핵심입니다. 기술보다 '무엇을 알고 싶은가'가 먼저입니다.",
   sample_extra_html(5, 1)),

  (5, 2, "2026-05-12 (화)", "텍스트 수집·LLM 파이프라인 (Cursor)",
   "계획서 5주차: 뉴스·공공데이터 메타데이터 등 텍스트 수집, LLM으로 공공·행정 관련 공개 데이터와 결합한 파이프라인 구성 — Cursor를 IDE로 활용합니다.",
   "Phase 2 – AI 툴 심화·개인 역량 (3~5주)",
   TIMELINES[(5, 2)],
   [("blue","계획서","Python+AI+Cursor"),
    ("purple","공공/정책","도메인 라벨 정의"),
    ("green","재현성","동일 입력 동일 출력"),
    ("orange","다음","Looker 또는 시각화")],
   ["collect_raw.py","pipeline_run.log","report.json"],
   ["pipeline.py","report.json"],
   "미니 프로젝트는 <strong>공공·행정 관련 공개 데이터와 텍스트</strong>를 다룹니다. 비공개·민감 데이터는 사용하지 않고, 출처를 항상 남기세요.",
   sample_extra_html(5, 2)),

  (5, 3, "2026-05-13 (수)", "Looker Studio 또는 시각화 연습",
   "계획서 5주차: Looker Studio 또는 시각화 도구로 파이프라인 결과를 연결·표현합니다.",
   "Phase 2 – AI 툴 심화·개인 역량 (3~5주)",
   TIMELINES[(5, 3)],
   [("blue","Looker","계획서 명시 옵션"),
    ("purple","대안","정적 차트+HTML"),
    ("green","스토리","한 장면에 한 메시지"),
    ("orange","다음","글로벌 벤치마크 리서치")],
   ["시각화 1종","스크린샷·캡션"],
   ["dashboard_w5.png","looker_notes_w5.md"],
   "계획서는 <strong>Looker Studio 또는 시각화</strong>를 병행합니다. 도구보다 '이 지표가 의사결정에 어떻게 쓰이는지'를 한 문장으로 적으세요.",
   sample_extra_html(5, 3)),

  (5, 4, "2026-05-14 (목)", "젠스파크 — 글로벌 AI·서비스 벤치마크 리서치",
   "계획서 5주차: 유사 서비스·산업 사례를 젠스파크로 조사한 뒤 AI로 비교·요약합니다. (공공·민간 가리지 않되 출처 명시)",
   "Phase 2 – AI 툴 심화·개인 역량 (3~5주)",
   TIMELINES[(5, 4)],
   [("blue","젠스파크","멀티소스 리서치"),
    ("purple","비교","공개 자료만"),
    ("green","연결","미니 PJ 기획서"),
    ("orange","공공·정책","2주차 사례 조사와 연결")],
   ["Sparkpage","벤치마크 메모"],
   ["benchmark_spark_w5.md","insights_policy_w5.md"],
   "이 날은 <strong>벤치마크 리서치 후 AI로 인사이트 정리</strong>(계획서 5주차 공통)까지가 한 세트입니다. 표만 만들지 말고, 개인 기획서에 넣을 문단으로 남기세요.",
   sample_extra_html(5, 4)),

  (5, 5, "2026-05-15 (금)", "미니 프로젝트 기획서 & 주간 정리",
   "계획서 5주차 핵심 산출물: 미니 프로젝트 기획서 — 리포트·시각화·글로벌 벤치마크를 통합합니다.",
   "Phase 2 – AI 툴 심화·개인 역량 (3~5주)",
   TIMELINES[(5, 5)],
   [("blue","산출물","계획서: 리포트+기획서"),
    ("purple","멘토","재량 조정 가능"),
    ("green","통합","파이프라인+시각화+리서치"),
    ("orange","6주차","프로젝트 구현 본격")],
   ["mini_project_plan_w5.pdf","feedback_w5.md","retrospective_w5.md"],
   ["mini_project_plan_w5.pdf","requirements_mini_project.md"],
   "계획서 5주차 마지막은 <strong>미니 프로젝트 기획서</strong>로 마무리합니다. 6주차에 바로 코드를 쓸 수 있도록 산출물 이름·경로까지 적어두세요.",
   sample_extra_html(5, 5)),

  # ────────────────── WEEK 6 (계획서: 미니 PJ 구현·문서화·중간점검·PPT·피드백) ──────────────────
  (6, 1, "2026-05-18 (월)", "미니 PJ 스프린트 1 — 기획서 대비 범위·환경",
   "계획서 6주차: 5주차 기획서를 기준으로 구현 우선순위·스프린트 목표를 고정하고, 저장소·브랜치·첫 이슈를 만듭니다.",
   "Phase 3 – 개인 미니 프로젝트·결과 (6~8주)",
   TIMELINES[(6, 1)],
   [("blue","기획서","단일 진실 공급원"),
    ("purple","Done","측정 가능한 완료 정의"),
    ("green","재현","동일 커맨드 동일 결과"),
    ("orange","커밋","작게 자주")],
   ["scope_w6.md","sprint_w6.md","README 실행 블록","첫 동작 커밋"],
   ["scope_w6.md","sprint_w6.md","README.md"],
   "6주차는 <strong>기획서에 없는 기능을 추가하지 않는 것</strong>이 첫 승리입니다. 막히면 멘토 미팅 전에 '질문 한 줄·시도한 것 두 줄'을 적어두세요.",
   sample_extra_html(6, 1)),

  (6, 2, "2026-05-19 (화)", "핵심 로직 구현 (Cursor + Python)",
   "계획서 6주차: 텍스트·데이터 파이프라인의 핵심(전처리·LLM 호출·JSON 출력)을 완성합니다.",
   "Phase 3 – 개인 미니 프로젝트·결과 (6~8주)",
   TIMELINES[(6, 2)],
   [("blue","파이프라인","한 단계씩 테스트"),
    ("purple","JSON","스키마 문서화"),
    ("green","품질","소량 검증 후 확대"),
    ("orange","키",".env만")],
   ["핵심 경로 end-to-end","검증 표","커밋·로그"],
   ["pipeline_core.py","validation_w6.md","report_partial.json"],
   "Cursor로 <strong>함수 단위로 쪼개서</strong> 짜면 디버깅이 빨라집니다. '한 번에 전부'보다 '입력 5줄이 나오면 성공' 같은 중간 목표를 두세요.",
   sample_extra_html(6, 2)),

  (6, 3, "2026-05-20 (수)", "Cowork·오픈클로로 문서·보고 자동화",
   "계획서 6주차: 구현 내용을 Cowork·오픈클로로 요약·README 초안·주간 진행 메모로 자동화합니다.",
   "Phase 3 – 개인 미니 프로젝트·결과 (6~8주)",
   TIMELINES[(6, 3)],
   [("blue","Cowork","긴 맥락 요약"),
    ("purple","오픈클로","반복 산출"),
    ("green","사람","사실 검증"),
    ("orange","산출물","멘토·검토자가 읽을 수 있게")],
   ["README 초안","progress 메모","다이어그램·캡처"],
   ["README.md","progress_w6.md","automation_doc_w6.md"],
   "문서 자동화는 <strong>초안을 뽑고 사람이 한 번 검증</strong>하는 흐름이 안전합니다. 내부 데이터·고객명은 절대 입력하지 마세요.",
   sample_extra_html(6, 3)),

  (6, 4, "2026-05-21 (목)", "중간 점검 — 데모·피드백 반영",
   "계획서 6주차: 멘토 앞에서 동작 데모를 하고, 피드백을 이슈로 바꿔 당일 또는 금요일까지 반영 범위를 정합니다.",
   "Phase 3 – 개인 미니 프로젝트·결과 (6~8주)",
   TIMELINES[(6, 4)],
   [("blue","데모","재현 가능하게"),
    ("purple","피드백","이슈화"),
    ("green","범위","한 건만 당일"),
    ("orange","기록","미팅 메모")],
   ["데모 성공","이슈 목록","반영 1건","mid_review_w6.md"],
   ["demo_script_w6.md","mid_review_w6.md","GitHub issues 또는 메모"],
   "중간 점검에서는 <strong>완성도보다 재현과 솔직한 막힘</strong>이 중요합니다. '안 된다'를 숨기지 말고, 시도한 것과 다음 실험을 말하세요.",
   sample_extra_html(6, 4)),

  (6, 5, "2026-05-22 (금)", "발표 스토리·PPT 초안 & 6주차 회고",
   "계획서 6주차: 미니 PJ 진행 상황을 발표용 스토리로 묶고 슬라이드 초안을 만들며, KPT로 7주차 완성·검증 계획으로 연결합니다.",
   "Phase 3 – 개인 미니 프로젝트·결과 (6~8주)",
   TIMELINES[(6, 5)],
   [("blue","스토리","한 슬라이드 한 메시지"),
    ("purple","숫자","추정이면 라벨"),
    ("green","회고","구체적 Try"),
    ("orange","7주차","완성·발표 준비")],
   ["presentation_w6_draft.pptx","story_w6.md","retrospective_w6.md","plan_w7.md"],
   ["presentation_w6_draft.pptx","retrospective_w6.md","plan_w7.md"],
   "슬라이드 초안은 <strong>임원용 한 문장 가치 제안</strong>이 있으면 나머지는 채워집니다. '무엇이 얼마나 나아졌는지' 숫자 또는 Before/After를 넣으세요.",
   sample_extra_html(6, 5)),

  # ────────────────── WEEK 7 (계획서: 완성·검증·PPT·피드백·최종 패키지) ──────────────────
  (7, 1, "2026-05-25 (월)", "기능 완성 & 엣지 케이스",
   "계획서 7주차: 미니 PJ의 핵심 시나리오를 끝까지 완주하고, 예외 입력·에러 메시지·로그를 정리합니다.",
   "Phase 3 – 개인 미니 프로젝트·결과 (6~8주)",
   TIMELINES[(7, 1)],
   [("blue","완주","한 사용자 흐름 끝까지"),
    ("purple","엣지","조용히 죽지 않기"),
    ("green","로그","재현에 충분한"),
    ("orange","태그","마일스톤")],
   ["3 시나리오 통과","에러 메시지 정리","회귀 표","커밋"],
   ["edge_cases_w7.md","regression_w7.md"],
   "계획서 흐름상 7주차는 <strong>데모 가능한 완성도</strong>가 목표입니다. 완벽한 제품이 아니라, 설명 가능한 범위와 한계가 명확한 산출물이면 됩니다.",
   sample_extra_html(7, 1)),

  (7, 2, "2026-05-26 (화)", "산출물 패키징 — README·폴더·라이선스",
   "계획서 7주차: 멘토가 재현할 수 있게 README, 폴더 구조, 샘플 데이터(공개 가능한 것만), 라이선스·출처를 정리합니다.",
   "Phase 3 – 개인 미니 프로젝트·결과 (6~8주)",
   TIMELINES[(7, 2)],
   [("blue","재현","동일 커맨드"),
    ("purple","샘플","민감정보 제로"),
    ("green","출처","투명성"),
    ("orange","패키지","한 번에 전달")],
   ["README 완성","sample 데이터","LICENSE","release zip"],
   ["README.md","LICENSE","data/sample/","docs/package_notes_w7.md"],
   "README 첫 줄에 <strong>이 프로젝트가 해결하는 문제</strong>를 쓰세요. 설치는 그 다음입니다.",
   sample_extra_html(7, 2)),

  (7, 3, "2026-05-27 (수)", "PPT 완성 & 데모 스크립트 동결",
   "계획서 7주차: 최종 발표용 슬라이드를 정리하고, 데모는 스크립트·백업(스크린샷/짧은 영상)까지 포함해 동결합니다.",
   "Phase 3 – 개인 미니 프로젝트·결과 (6~8주)",
   TIMELINES[(7, 3)],
   [("blue","슬라이드","한 장 한 메시지"),
    ("purple","데모","리허설과 동일"),
    ("green","백업","플랜 B"),
    ("orange","PDF","공유용")],
   ["PPT v2","데모 스크립트","백업 자료"],
   ["presentation_w7_v2.pptx","demo_script_final.md","demo_backup_w7.mp4"],
   "발표 자료는 <strong>청중이 기억할 한 문장</strong>을 먼저 정하고 슬라이드를 거꾸로 채우면 흐름이 잡힙니다.",
   sample_extra_html(7, 3)),

  (7, 4, "2026-05-28 (목)", "리허설·Q&A·멘토 피드백 반영",
   "계획서 7주차: 15+5분 형식으로 리허설하고, 질문 목록과 답 초안을 만든 뒤 슬라이드·데모에 반영합니다.",
   "Phase 3 – 개인 미니 프로젝트·결과 (6~8주)",
   TIMELINES[(7, 4)],
   [("blue","시간","엄수"),
    ("purple","Q&A","짧고 정직하게"),
    ("green","피드백","선택만 반영"),
    ("orange","8주차","최종 발표만 남김")],
   ["리허설 1회","Q&A 문서","피드백 반영","qa_final_w7.md"],
   ["presentation_w7_v3.pptx","qa_final_w7.md"],
   "리허설에서 <strong>시간 초과분은 슬라이드에서 잘라내는 것</strong>이 맞습니다. 말을 늘리지 않으면 신뢰가 올라갑니다.",
   sample_extra_html(7, 4)),

  (7, 5, "2026-05-29 (금)", "7주차 회고 & 8주차(최종·수료) 준비",
   "계획서 7주차: KPT로 정리하고, 8주차 최종 발표·회고 보고서·아이뱅크 제안·면담 일정을 확인합니다.",
   "Phase 3 – 개인 미니 프로젝트·결과 (6~8주)",
   TIMELINES[(7, 5)],
   [("blue","회고","솔직함"),
    ("purple","8주차","일정·산출물"),
    ("green","아이뱅크","제안 초안 예고"),
    ("orange","컨디션","과로 금지")],
   ["retrospective_w7.md","checklist_w8.md","reflection_outline.md"],
   ["retrospective_w7.md","checklist_w8.md","reflection_outline.md"],
   "7주차 마지막은 <strong>8주차의 산출물 이름과 마감</strong>을 캘린더에 박아 두는 날입니다. 발표 전날에 새로 쓰지 않도록 회고 목차만 잡아두면 충분합니다.",
   sample_extra_html(7, 5)),

  # ────────────────── WEEK 8 (계획서: 최종 발표·회고 보고서·아이뱅크 제안·면담·GitHub/블로그) ──────────────────
  (8, 1, "2026-06-01 (월)", "최종 발표 리허설 & 수치·슬라이드 동결",
   "계획서 8주차: 최종 발표 전 마지막 리허설과 산출물 수치 확정, 슬라이드·데모·백업을 동결합니다.",
   "Phase 3 – 개인 미니 프로젝트·결과 (6~8주)",
   TIMELINES[(8, 1)],
   [("blue","수치","검증된 것만"),
    ("purple","동결","더 이상 안 고침"),
    ("green","백업","플랜 B"),
    ("orange","컨디션","수면")],
   ["performance_metrics_w8.md","presentation_final_w8.pdf","demo_checklist_w8.md"],
   ["presentation_final_w8.pdf","performance_metrics_w8.md","demo_backup_final.mp4"],
   "최종 발표 전날은 <strong>새 기능 금지</strong>입니다. 숫자와 데모만 믿을 수 있게 만드세요.",
   sample_extra_html(8, 1)),

  (8, 2, "2026-06-02 (화)", "🎉 최종 발표",
   "계획서 8주차: 8주간의 미니 프로젝트와 AI 업무 경험을 발표합니다 — 문제·접근·결과·한계·배움을 한 흐름으로.",
   "Phase 3 – 개인 미니 프로젝트·결과 (6~8주)",
   TIMELINES[(8, 2)],
   [("blue","발표","첫 문장 임팩트"),
    ("purple","정직","한계 인정"),
    ("green","기록","피드백"),
    ("orange","회고","이어쓰기")],
   ["발표 완료","피드백 메모","회고 초안 시작"],
   ["presentation_final_w8.pdf","feedback_final_w8.md","reflection_report_draft.md"],
   "발표에서 <strong>한계와 윤리(데이터·출처)</strong>를 짧게 말하면 신뢰가 올라갑니다. 완벽한 결과보다 투명한 설명이 남습니다.",
   sample_extra_html(8, 2)),

  (8, 3, "2026-06-03 (수)", "회고 보고서 완성",
   "계획서 8주차 핵심 산출물 중 하나: 회고 보고서 — 배경·학습·성과·한계·향후 과제를 문서로 남깁니다.",
   "Phase 3 – 개인 미니 프로젝트·결과 (6~8주)",
   TIMELINES[(8, 3)],
   [("blue","회고","솔직함"),
    ("purple","수치","출처"),
    ("green","도구","편향·한계"),
    ("orange","향후","다음 한 걸음")],
   ["8주 한 줄 요약","도구 성찰","최종 PDF"],
   ["reflection_report_final.pdf","weekly_one_liners_w8.md"],
   "회고 보고서는 <strong>자기 홍보가 아니라 학습의 증거</strong>입니다. 안 됐던 시도도 가치 있습니다.",
   sample_extra_html(8, 3)),

  (8, 4, "2026-06-04 (목)", "회사(아이뱅크) 제안서 초안 & 평가 면담 준비",
   "계획서 8주차: 인턴 기간 인사이트를 회사(아이뱅크)에 제안할 수 있는 형태로 정리하고, 평가·면담 질문을 준비합니다.",
   "Phase 3 – 개인 미니 프로젝트·결과 (6~8주)",
   TIMELINES[(8, 4)],
   [("blue","아이뱅크","맥락에 맞는 제안"),
    ("purple","근거","공개 정보·본인 실험"),
    ("green","현실성","작은 파일럿"),
    ("orange","면담","질문이 대화를 연다")],
   ["proposal_ibank_draft.pdf","exec_summary_1p_w8.md","interview_questions_w8.md"],
   ["proposal_ibank_draft.pdf","interview_questions_w8.md"],
   "제안서는 <strong>큰 그림 한 장 + 실행 가능한 다음 한 걸음</strong>이 있으면 충분합니다. 모든 것을 고치겠다고 쓰지 마세요.",
   sample_extra_html(8, 4)),

  (8, 5, "2026-06-05 (금)", "🎓 수료 · GitHub·블로그 · 감사 · 마무리 면담",
   "계획서 8주차 마무리: 공식 일정에 맞춰 수료를 정리하고, GitHub·블로그(선택)로 공개 가능한 포트폴리오를 남기며 감사 인사와 마무리 면담으로 프로그램을 닫습니다.",
   "Phase 3 – 개인 미니 프로젝트·결과 (6~8주)",
   TIMELINES[(8, 5)],
   [("blue","포트폴리오","재현 가능"),
    ("purple","공개","비밀 없는 것만"),
    ("green","관계","감사와 존중"),
    ("orange","다음","로드맵 첫 주")],
   ["GitHub 공개 확인","블로그 또는 요약","감사 메시지","closing_notes_w8.md"],
   ["README.md (public)","blog_or_summary_w8.md","closing_notes_w8.md"],
   "프로그램의 끝은 <strong>저장소와 관계의 정리</strong>입니다. 8주는 짧고, 남는 것은 문서와 사람에게 받은 말입니다.",
   sample_extra_html(8, 5)),
]

# ── DAY 레이블 ─────────────────────────────────────────────────
DAY_LABELS = {(w, d): f"W{w}D{d} – {title}"
              for (w, d, _, title, *_rest) in PAGES}

def get_nav(week, day):
    keys = [(p[0], p[1]) for p in PAGES]
    idx  = keys.index((week, day))
    def path(k):
        w, d = k
        return f"day{d}.html" if w == week else f"../week{w}/day{d}.html"
    prev_k = keys[idx-1] if idx > 0 else None
    next_k = keys[idx+1] if idx < len(keys)-1 else None
    return (
        path(prev_k) if prev_k else "../index.html",
        DAY_LABELS.get(prev_k, "🏠 대시보드"),
        path(next_k) if next_k else "../index.html",
        DAY_LABELS.get(next_k, "🏠 대시보드"),
    )

def tl(items):
    h = '<div class="timeline">'
    for t, ti, d in items:
        h += f'<div class="tl-item"><div class="tl-time">{t}</div><div class="tl-title">{ti}</div><div class="tl-desc">{d}</div></div>'
    return h + '</div>'

def cards(items):
    h = '<div class="cards-grid">'
    for c, ti, d in items:
        h += f'<div class="card {c}"><h3>{ti}</h3><p>{d}</p></div>'
    return h + '</div>'

def checklist(items):
    h = '<div class="checklist"><ul>'
    for i in items:
        h += f'<li>{CHECK_SVG}{i}</li>'
    return h + '</ul></div>'

def output_box(items):
    h = f'<div class="output-box"><h3>{OUT_SVG} 오늘의 산출물</h3><ul>'
    for i in items:
        h += f'<li>{i}</li>'
    return h + '</ul></div>'

def build(week, day, date, title, subtitle, phase,
          tl_items, card_items, cl_items, out_items, tip, extra):
    pp, pl, np_, nl = get_nav(week, day)
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>W{week}D{day} - {title}</title>
<style>{COMMON_CSS}</style>
</head>
<body>
<nav class="topnav">
  {HOME_SVG}
  <div class="breadcrumb">
    <a href="../index.html">홈</a> · <a href="../calendar.html">캘린더</a> › <a href="day1.html">{week}주차</a> › <span>Day {day} – {title}</span>
  </div>
</nav>
<div class="hero">
  <div class="meta">
    <span class="chip week">{week}주차</span>
    <span class="chip day">DAY {day}</span>
    <span class="chip date">📅 {date}</span>
    <span class="chip phase">🔬 {phase}</span>
  </div>
  <h1><span>{title}</span></h1>
  <p>{subtitle}</p>
</div>
<div class="container">
  <div class="section-title">{CLOCK_SVG} 일일 스케줄</div>
  {tl(tl_items)}
  <div class="section-title">{GRID_SVG} 핵심 내용</div>
  {cards(card_items)}
  {extra}
  <div class="tip-box">{TIP_SVG}<p>💡 <strong>오늘의 팁:</strong> {tip}</p></div>
  <div class="section-title">{EDIT_SVG} 오늘의 체크리스트</div>
  {checklist(cl_items)}
  {output_box(out_items)}
  <div class="day-nav">
    <a href="{pp}">{PREV_SVG} {pl}</a>
    <div class="day-nav-mid">
      <a href="../index.html">🏠 대시보드</a>
      <a href="../calendar.html">📅 캘린더 보기</a>
    </div>
    <a href="{np_}">{nl} {NEXT_SVG}</a>
  </div>
</div>
</body>
</html>"""

# ── index.html 생성 ────────────────────────────────────────────
INDEX_HTML = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI 인턴십 8주 프로그램 대시보드</title>
<style>
  :root{--primary:#6c63ff;--dark:#1a1a2e;--card:#16213e;--card2:#0f3460;--text:#e0e0e0;--muted:#a0a0b0;}
  *{margin:0;padding:0;box-sizing:border-box;}
  body{background:var(--dark);color:var(--text);font-family:'Segoe UI',sans-serif;}
  header{background:linear-gradient(135deg,#0f3460,#1a1a2e);padding:48px 32px;text-align:center;border-bottom:2px solid var(--primary);}
  header h1{font-size:2.2rem;font-weight:900;margin-bottom:10px;}
  header h1 span{color:var(--primary);}
  header p{color:var(--muted);font-size:1rem;}
  .meta-row{display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin-top:18px;}
  .meta-chip{background:var(--card);border:1px solid #ffffff18;border-radius:20px;padding:6px 16px;font-size:.82rem;color:var(--muted);}
  .container{max-width:1100px;margin:0 auto;padding:40px 24px;}
  .week-block{margin-bottom:40px;}
  .week-header{display:flex;align-items:center;gap:12px;margin-bottom:16px;padding-bottom:12px;border-bottom:2px solid var(--primary);opacity:.8;}
  .week-header h2{font-size:1.2rem;font-weight:800;}
  .week-phase{font-size:.78rem;color:var(--muted);background:var(--card);padding:3px 12px;border-radius:12px;border:1px solid #ffffff18;}
  .day-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;}
  .day-card{background:var(--card);border:1px solid #ffffff12;border-radius:10px;padding:16px 12px;text-align:center;transition:.2s;cursor:pointer;}
  .day-card:hover{background:var(--card2);border-color:var(--primary);transform:translateY(-2px);}
  .day-card a{text-decoration:none;color:inherit;display:block;}
  .day-label{font-size:.72rem;color:var(--muted);margin-bottom:4px;}
  .day-title{font-size:.82rem;font-weight:700;color:var(--text);}
  .day-num{width:28px;height:28px;background:var(--primary);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.75rem;font-weight:800;margin:0 auto 8px;}
  .phase-legend{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:28px;}
  .legend-item{display:flex;align-items:center;gap:6px;font-size:.8rem;color:var(--muted);}
  .legend-dot{width:10px;height:10px;border-radius:50%;}
  @media(max-width:600px){.day-grid{grid-template-columns:repeat(3,1fr);}}
</style>
</head>
<body>
<header>
  <h1>🤖 AI 업무 경험 <span>8주 프로그램</span></h1>
  <p>미래내일 일경험(인턴형) · 아이뱅크 · Claude Cowork · Cursor · 젠스파크 · 오픈클로 — 계획서 최종 기준</p>
  <div class="meta-row">
    <span class="meta-chip">🎯 개인 미니 PJ (후보 4종): VOC 대시보드 · RAG 챗봇 · 트렌드 브리핑 · 업무 자동화</span>
    <span class="meta-chip">📅 2026.04.13 ~ 2026.06.05</span>
    <span class="meta-chip">⏱ 평일 13:00–18:00 (5시간/일) · 주 25시간 · 오프라인 중심</span>
    <span class="meta-chip">👤 멘토 조준형 · 미니 프로젝트는 인턴 개별 수행</span>
    <span class="meta-chip">📣 주간 멘토 미팅 30분 + 개인 데일리 체크인 15분</span>
  </div>
</header>
<div class="container">
  <div class="phase-legend">
    <div class="legend-item"><div class="legend-dot" style="background:#40c4ff"></div>Phase 1 — 탐색·AI 환경 구축 (1~2주)</div>
    <div class="legend-item"><div class="legend-dot" style="background:#7c4dff"></div>Phase 2 — AI 툴 심화·개인 역량 (3~5주)</div>
    <div class="legend-item"><div class="legend-dot" style="background:#00e676"></div>Phase 3 — 개인 미니 프로젝트·결과 (6~8주)</div>
  </div>
  <p style="text-align:center;margin:0 0 28px;font-size:.9rem;color:#a0a0b0;">📅 <a href="calendar.html" style="color:#6c63ff;font-weight:600;">주차별 캘린더</a> (월별 한눈에 보기) · 📎 <a href="../intern-documents/docs/README.md" style="color:#6c63ff;font-weight:600;">업무일지·문서 양식</a> (Markdown) — 일지, 주간요약, 멘토 미팅, KPT, 미니 PJ 기획서, 회고 보고서 목차</p>
"""

WEEK_META = [
  (1,"온보딩·환경 (계획서 1주)","#40c4ff",
   ["온보딩·OT","Claude·Cursor","젠스파크·오픈클로","LLM 동향 과제","주간미팅·일지"]),
  (2,"트렌드·산업 사례 (2주)","#40c4ff",
   ["심화 리서치","산업·서비스 사례","Cowork WF","프롬프트 기초","보고서 1차·피드백"]),
  (3,"Cursor·API (3주)","#7c4dff",
   ["코딩 실습","GA4·자동화","API 파이프라인","Few-shot·CoT","스크립트+가이드"]),
  (4,"업무 자동화 (4주)","#7c4dff",
   ["Cowork 자동화","반복 리포트","오픈클로 템플릿","툴 비교","미니 PJ 주제 확정"]),
  (5,"데이터·기획서 (5주)","#00e676",
   ["텍스트·파이프라인","공개데이터·Cursor","Looker·시각화","글로벌 벤치마크","미니 PJ 기획서"]),
  (6,"미니 프로젝트 (6주)","#ffab00",
   ["스프린트·환경","핵심 파이프라인","Cowork·문서","중간 점검","PPT·6주 회고"]),
  (7,"완성·발표 준비 (7주)","#f50057",
   ["완성·엣지","패키징·README","PPT·데모 동결","리허설·Q&A","7주 회고·8주 준비"]),
  (8,"최종·수료 (8주)","#f50057",
   ["발표 리허설","🎉 최종 발표","회고 보고서","아이뱅크 제안·면담","🎓 수료·GitHub"]),
]

for wnum, phase, color, days in WEEK_META:
    INDEX_HTML += f"""
  <div class="week-block">
    <div class="week-header">
      <div style="width:4px;height:24px;background:{color};border-radius:2px;"></div>
      <h2>{wnum}주차</h2>
      <span class="week-phase">{phase}</span>
    </div>
    <div class="day-grid">"""
    for i, dtitle in enumerate(days, 1):
        INDEX_HTML += f"""
      <div class="day-card">
        <a href="week{wnum}/day{i}.html">
          <div class="day-num">{i}</div>
          <div class="day-label">{'월화수목금'[i-1]}요일</div>
          <div class="day-title">{dtitle}</div>
        </a>
      </div>"""
    INDEX_HTML += "\n    </div>\n  </div>"

INDEX_HTML += """
</div>
</body>
</html>"""

# ── 메인 실행 ──────────────────────────────────────────────────
def main():
    base = str(PROG_ROOT / "intern-program")
    os.makedirs(base, exist_ok=True)

    # index.html
    with open(os.path.join(base, "index.html"), "w", encoding="utf-8") as f:
        f.write(INDEX_HTML)
    print("✅ index.html 생성 완료")

    # 주차별 day 파일
    count = 0
    for page in PAGES:
        week, day = page[0], page[1]
        folder = os.path.join(base, f"week{week}")
        os.makedirs(folder, exist_ok=True)
        html = build(*page)
        path = os.path.join(folder, f"day{day}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ week{week}/day{day}.html — {page[3]}")
        count += 1

    print(f"\n{'='*50}")
    print(f"🎉 완료! 총 {count}개 HTML + index.html 생성")
    print(f"📁 경로: {os.path.abspath(base)}")
    print(f"🌐 브라우저에서 intern-program/index.html 열기")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
