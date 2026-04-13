# 1주차 일일 타임라인 (13:00–18:00 상세) — generate_pages.py에서 import

TIMELINES = {
    (1, 1): [
        ("13:00–14:00", "프로그램·일정·OT 연계 안내",
         "① <strong>자리·장비</strong> — 노트북 전원·네트워크·화면 공유 테스트<br>"
         "② <strong>프로그램 취지</strong> — 미래내일 일경험(인턴형), 8주·산출물(리포트·발표)·주 25h를 한 슬라이드 또는 메모에 정리<br>"
         "③ <strong>로드맵</strong> — Phase1~3·미니 PJ 주차를 타임라인에 적기<br>"
         "④ <strong>멘토</strong> — 조준형님·소통 채널(Slack/메일)·응답 SLA 기대치 확인<br>"
         "⑤ <strong>보안</strong> — 일지·산출물 제출 경로, 내부 자료 취급 금지 범위<br>"
         "⑥ <strong>체크</strong> — 오늘 말한 목표가 내일 일지 첫 줄과 맞는지"),
        ("14:00–15:00", "부서·업무 파악",
         "① <strong>조직도 메모</strong> — 팀명·담당 업무 한 줄씩<br>"
         "② <strong>소통 툴</strong> — 메일·슬랙·노션·승인 시스템 중 실제 쓰는 것만<br>"
         "③ <strong>요청 흐름</strong> — 누구에게 어떤 형식으로 요청하는지 예시 1건<br>"
         "④ <strong>기여 후보</strong> — 인턴 기간에 해볼 만한 과제 3가지(현실적 범위)<br>"
         "⑤ <strong>기록</strong> — 부서 메모를 `goal_plan` 초안에 붙일 문단으로"),
        ("15:00–16:00", "인턴 목표·계획 (SMART)",
         "① <strong>계획서 §2.2</strong> — AI 트렌드·툴·미니 PJ·포트폴리오 중 본인 우선순위 표시<br>"
         "② <strong>SMART</strong> — 구체적·측정·달성가능·관련·기한을 표로 3줄<br>"
         "③ <strong>OT 연계</strong> — 부서 목표 문장과 한 줄로 연결<br>"
         "④ <strong>검증</strong> — 한 달 뒤 멘토가 물어볼 질문 3개 예상하고 답 초안<br>"
         "⑤ <strong>파일</strong> — `goal_plan_w1d1.md` 파일명으로 저장 시작"),
        ("16:00–17:00", "최신 LLM·생성형 AI 개요",
         "① <strong>표 헤더</strong> — GPT-4o / Claude 3.x / Gemini 2.x / (선택) 로컬·온디바이스<br>"
         "② <strong>열</strong> — 강점·약점·맥락 길이·API·비용 느낌(공개 자료만)<br>"
         "③ <strong>공공·행정</strong> — 민원 챗봇·문서요약·다국어 등 키워드 한 줄씩<br>"
         "④ <strong>출처</strong> — 각 칸에 링크 또는 문서명+날짜<br>"
         "⑤ <strong>저장</strong> — `llm_overview_w1.md` 초안"),
        ("17:00–18:00", "일지 양식·내일 준비",
         "① <strong>템플릿</strong> — `journal_template.md` 복사 → `journal_2026-04-13.md` 등 날짜 파일명 규칙 결정<br>"
         "② <strong>항목</strong> — 목표·시간대·이슈·질문·산출물 칸 확인<br>"
         "③ <strong>내일</strong> — Cowork·Cursor 설치 체크리스트 URL·용량 확인<br>"
         "④ <strong>질문</strong> — 멘토에게 물을 것 1개를 미리 적기"),
    ],
    (1, 2): [
        ("13:00–14:00", "Claude Cowork — 설치부터 첫 대화까지",
         "① <strong>개념</strong> — Cowork는 브라우저만이 아니라 <strong>데스크톱 에이전트</strong>로 폴더·파일을 읽고 초안을 쓰는 도구임을 한 줄로 메모<br>"
         "② <strong>다운로드·설치</strong> — 공식 채널에서 OS에 맞는 앱 설치 → 실행 → 업데이트 있으면 적용<br>"
         "③ <strong>로그인</strong> — Claude/Anthropic 계정 또는 회사에서 안내한 SSO·초대 링크로 로그인 (막히면 스크린샷·에러 문구만 캡처, 비밀번호는 금지)<br>"
         "④ <strong>워크스페이스</strong> — 새 워크스페이스 생성 → 이름 규칙 예: <code>intern_w1_ai_setup</code><br>"
         "⑤ <strong>샘플 파일</strong> — 연습용 <code>.txt</code> 또는 짧은 <code>.md</code> 1개를 워크스페이스에 넣기 (공개 가능한 텍스트만)<br>"
         "⑥ <strong>첫 프롬프트</strong> — 「이 문서를 읽고 핵심만 3줄로 요약해 줘. 각 줄 끝에 근거가 된 문장을 괄호로 표시해 줘.」<br>"
         "⑦ <strong>검증</strong> — 응답이 나오면: 요약 3줄 존재 여부, 환각이면 「모른다」로 고치도록 한 번 더 요청해 보기<br>"
         "⑧ <strong>기록</strong> — 사용한 모델명·대략 소요 시간·막힌 단계를 <code>cowork_first_session.md</code>에 적기 시작"),
        ("14:00–15:00", "Cursor IDE — 설치·익스텐션·첫 코드",
         "① <strong>설치</strong> — cursor.com 에서 OS용 설치 파일 받기 → 설치 → 실행<br>"
         "② <strong>계정</strong> — Cursor 계정 로그인(또는 GitHub 연동) — 팀 정책 있으면 안내대로<br>"
         "③ <strong>Python</strong> — 로컬에 Python 3.10+ 설치 여부 확인 — 터미널에서 <code>python3 --version</code> — 없으면 python.org 또는 회사 표준 경로로 설치<br>"
         "④ <strong>익스텐션</strong> — Python / Pylance(또는 회사 권장 목록) 설치 — JS는 차주로 미룰 수 있음<br>"
         "⑤ <strong>인터프리터</strong> — Command Palette → Python 인터프리터 선택 → venv는 <code>python -m venv .venv</code> 후 지정<br>"
         "⑥ <strong>AI 설정</strong> — Cursor 설정에서 모델·Tab 완성 — 회사 허용 모델만<br>"
         "⑦ <strong>첫 파일</strong> — <code>hello_w1d2.py</code> → <code>print(\"ok\")</code> 실행 확인<br>"
         "⑧ <strong>Tab</strong> — 주석 한 줄 후 Tab 제안 수락/거절 연습<br>"
         "⑨ <strong>메모</strong> — <code>cursor_setup_notes.md</code>에 버전·경로·이슈"),
        ("15:00–16:00", "Cowork ↔ Cursor 역할 구분 · 미니 실습",
         "① <strong>규칙 5줄</strong> — (1) 긴 문서·리포트 초안은 Cowork (2) 코드·API는 Cursor (3) 산출물 폴더 <code>docs/</code> vs <code>src/</code> … 본인 문장으로<br>"
         "② <strong>샘플 텍스트</strong> — 공개 뉴스/보도 1페이지 → <code>sample.txt</code><br>"
         "③ <strong>Cowork</strong> — 「불릿 5개 + 한 문단 요약」→ 응답 복사<br>"
         "④ <strong>Cursor</strong> — <code>sample_notes.py</code> 또는 <code>notes.md</code>에 붙여넣기 → 주석으로 출처 표시 → 각 불릿에 「코드로 검증 가능?」 코멘트<br>"
         "⑤ <strong>정리</strong> — 규칙 5줄을 한 파일로 저장"),
        ("16:00–17:00", "계정·보안 · API 키·캡처",
         "① <strong>2FA</strong> — Claude·Cursor·GitHub 등 2단계 인증 켜기 — 백업 코드 안전 보관<br>"
         "② <strong>API 키</strong> — 코드에 직접 쓰지 않음 — <code>.env</code> + <code>.gitignore</code> — <code>.env.example</code>에 키 이름만<br>"
         "③ <strong>저장소</strong> — 테스트 repo가 있으면 private·초대자 확인<br>"
         "④ <strong>스크린샷</strong> — 이메일·토큰·내부명 가리기<br>"
         "⑤ <strong>회사 데이터</strong> — Cowork/Cursor에 넣기 전 규정 확인 — 불확실하면 공개 샘플만"),
        ("17:00–18:00", "오늘 로그 · 이슈 · 멘토 질문",
         "① <strong>일지</strong> — 오늘 5구간 채움·산출물 파일명<br>"
         "② <strong>이슈</strong> — <code>open_questions_w1.md</code>에 재현 순서<br>"
         "③ <strong>질문 3개</strong> — 금요일 미팅용·우선순위·시도한 것 한 줄<br>"
         "④ <strong>폴더</strong> — 오늘 md/py 한 곳에 모으기 — 내일 젠스파크 전 백업"),
    ],
    (1, 3): [
        ("13:00–14:00", "젠스파크 — 계정·첫 Sparkpage",
         "① <strong>가입·로그인</strong> — 공식 절차·회사 이메일 허용 여부 확인<br>"
         "② <strong>UI 둘러보기</strong> — 검색·Sparkpage·에이전트 메뉴 위치 메모<br>"
         "③ <strong>검색</strong> — 「생성형 AI 공공 행정 디지털 정부 도입 사례」등 계획서 키워드로 1회 실행<br>"
         "④ <strong>Sparkpage</strong> — 새 페이지 → 제목·출처 링크가 보이게 정리<br>"
         "⑤ <strong>저장·공유</strong> — URL 복사 → <code>genspark_sparkpage_w1.md</code>에 링크·한 줄 요약<br>"
         "⑥ <strong>이슈</strong> — 막히면 스크린샷·시간 기록"),
        ("14:00–15:00", "오픈클로 — 계정·첫 플로우",
         "① <strong>가입·워크스페이스</strong> — 오픈클로 계정·팀 초대 여부<br>"
         "② <strong>개념</strong> — 트리거 → 액션 체인을 그림으로 한 번 그리기<br>"
         "③ <strong>최소 플로우</strong> — 수동 트리거 1개 → 텍스트 입력 → 요약 또는 메모 저장 2액션<br>"
         "④ <strong>테스트</strong> — 샘플 문장으로 end-to-end<br>"
         "⑤ <strong>캡처</strong> — <code>openclaro_first_workflow.png</code> — 민감정보 가림"),
        ("15:00–16:00", "Genspark → Cowork 연결",
         "① <strong>복사</strong> — Sparkpage 본문 전체 또는 핵심 단락을 Cowork에 붙여넣기<br>"
         "② <strong>프롬프트</strong> — 「핵심 5불릿 + 각 불릿 근거 URL 또는 문장 + 출처 검증 요청」<br>"
         "③ <strong>검증</strong> — 환각이면 「근거 없으면 '확인 필요'로 표시」재요청<br>"
         "④ <strong>저장</strong> — 결과를 `.md`로 로컬 저장 — 파일명 규칙 통일<br>"
         "⑤ <strong>메모</strong> — 연동 시 막힌 점을 일지에"),
        ("16:00–17:00", "오픈클로 → 파일·드라이브 출력",
         "① <strong>내보내기</strong> — 오픈클로에서 요약 텍스트를 파일·구글 드라이브·메일 중 하나로 전송 시도<br>"
         "② <strong>실패 시</strong> — 수동 복사 단계를 순서도로 — `handoff_note`에<br>"
         "③ <strong>경로</strong> — 로컬이면 `exports/` 폴더 생성<br>"
         "④ <strong>검증</strong> — 파일 열어 인코딩·깨짐 확인"),
        ("17:00–18:00", "4툴 체크리스트·다음 주 키워드",
         "① <strong>표</strong> — Claude Cowork / Cursor / 젠스파크 / 오픈클로 — 설치 ✓·로그인 ✓·첫 성공 ✓·이슈<br>"
         "② <strong>tool_checklist_w1.md</strong> — 위 표 붙여넣기<br>"
         "③ <strong>키워드 5개</strong> — 2주차 심화 리서치용 — 예: 행정 챗봇·RAG·AI 거버넌스<br>"
         "④ <strong>질문 1개</strong> — 월요일 멘토·동료에게 물을 한 문장"),
    ],
    (1, 4): [
        ("13:00–14:00", "과제 범위·산출물 정의",
         "① <strong>계획서 대조</strong> — 비교 항목: 멀티모달·컨텍스트·API·비용·보안<br>"
         "② <strong>분량</strong> — A4 2~4페이지 또는 동등 분량 md<br>"
         "③ <strong>표지 정보</strong> — 제목·날짜·본인 이름·멘토명<br>"
         "④ <strong>금지</strong> — 내부 미공개 수치·고객명 금지<br>"
         "⑤ <strong>목차</strong> — 서론·3모델 비교·공공 사례·결론·참고문헌"),
        ("14:00–15:00", "Genspark 1차 리서치",
         "① <strong>쿼리</strong> — `GPT-4o 2026 enterprise` 등 연도 포함 검색 2회 이상<br>"
         "② <strong>Sparkpage</strong> — 최소 2개 — 국내·해외 또는 제품·정책 구분<br>"
         "③ <strong>메타</strong> — 각 Sparkpage에 출처·날짜 필드 채우기<br>"
         "④ <strong>저장</strong> — `sparkpage_refs_w1/` 폴더에 링크 목록 md"),
        ("15:00–16:00", "Cowork로 비교 초안",
         "① <strong>붙여넣기</strong> — Sparkpage 요약·표를 Cowork에<br>"
         "② <strong>표 요청</strong> — 행: GPT-4o / Claude / Gemini — 열: 강점·주의·추천 업무<br>"
         "③ <strong>공공·행정</strong> — 민원·문서요약·공공데이터 질의 예시 한 줄씩<br>"
         "④ <strong>편집</strong> — 중복 문장 제거·톤 통일"),
        ("16:00–17:00", "Cursor로 인용·코드 링크 수집",
         "① <strong>공개 예제</strong> — GitHub·문서에서 API 호출 예제 URL만 수집(실행은 차주)<br>"
         "② <strong>README</strong> — `참고 링크` 섹션에 bullet<br>"
         "③ <strong>주석</strong> — 각 링크가 어떤 실험에 쓰일지 한 줄"),
        ("17:00–18:00", "과제 초안 저장·TODO",
         "① <strong>파일</strong> — `llm_trend_assignment_w1.md` 또는 PDF 내보내기<br>"
         "② <strong>TODO</strong> — 보강할 표·출처·그림에 `[TODO]` 표시<br>"
         "③ <strong>백업</strong> — 클라우드·깃에 푸시(민감 제외)<br>"
         "④ <strong>내일</strong> — 금요일 패키징용 파일 이름 확정"),
    ],
    (1, 5): [
        ("13:00–14:00", "산출물 패키징",
         "① <strong>폴더</strong> — `deliverables_w1/` — 하위에 day1~day5·과제·일지<br>"
         "② <strong>목록</strong> — README 한 페이지에 파일명·설명 표<br>"
         "③ <strong>이름 규칙</strong> — `w1d3_genspark.md` 형태로 통일<br>"
         "④ <strong>압축</strong> — zip 또는 드라이브 링크 — 권한 안내"),
        ("14:00–15:00", "멘토 주간 미팅 (30분)",
         "① <strong>구조</strong> — 성과 5분·질문 10분·피드백 15분 권장<br>"
         "② <strong>데모</strong> — 환경 셋업·Sparkpage·과제 초안 중 1개만 짧게<br>"
         "③ <strong>합의</strong> — 2주차 「공공·행정 AI 도입 사례」범위·키워드<br>"
         "④ <strong>기록</strong> — `feedback_w1.md`에 bullet — 액션 ID 부여"),
        ("15:00–16:00", "피드백 반영",
         "① <strong>우선순위</strong> — 피드백을 번호 매기기 — 이번 주말 전 가능한 것만 체크<br>"
         "② <strong>LLM 과제</strong> — 보완 3가지를 과제 문서에 반영<br>"
         "③ <strong>질문</strong> — 이해 안 된 피드백은 질문으로 남기기"),
        ("16:00–17:00", "KPT (1주차)",
         "① <strong>Keep</strong> — 잘된 것 2가지 이상 — 구체적 행동<br>"
         "② <strong>Problem</strong> — 사실만 — 추측과 구분<br>"
         "③ <strong>Try</strong> — 다음 주 측정 가능한 행동 2가지<br>"
         "④ <strong>저장</strong> — `retrospective_w1.md`"),
        ("17:00–18:00", "2주차 프리프",
         "① <strong>키워드</strong> — 행정 챗봇·문서요약·민원 분류·공공데이터·RAG 등 5개<br>"
         "② <strong>월요일</strong> — 첫 활동: 심화 리서치 시나리오 한 단락 스케치<br>"
         "③ <strong>휴식</strong> — 과로 방지"),
    ],
}
