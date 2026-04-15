# Cursor 단축키 & 워크플로 가이드 — W3D1

**날짜:** 2026-04-27 (월)  
**일정:** W3D1 — Cursor + Python AI 코딩 실습  
**작성자:** 인턴  
**상태:** 작성 완료

---

## 1. 편집 단축키

| 단축키 | 기능 | 사용 빈도 |
|--------|------|-----------|
| `Cmd+K` | 인라인 AI 편집 (선택 후) | ★★★★★ |
| `Cmd+L` | AI 채팅 열기 | ★★★★★ |
| `Tab` | AI 코드 완성 수락 | ★★★★★ |
| `Esc` | AI 제안 거절 | ★★★★☆ |
| `Cmd+Shift+P` | 명령 팔레트 | ★★★★☆ |
| `Cmd+/` | 라인 주석 토글 | ★★★☆☆ |
| `Option+Up/Down` | 라인 위/아래 이동 | ★★★☆☆ |
| `Cmd+D` | 같은 단어 순차 선택 | ★★★☆☆ |

## 2. 터미널 단축키

| 단축키 | 기능 |
|--------|------|
| `` Ctrl+` `` | 터미널 열기/닫기 |
| `Cmd+Shift+5` | 터미널 창 분할 |
| `Cmd+1~9` | 에디터 탭 전환 |

## 3. Cursor Agent 사용법

### @멘션 참조
```
@utils.py 에서 load_csv 함수를 리팩터해줘. 예외처리 추가하고
타입 힌트도 붙여줘.
```

### Agent 모드 활용
- **파일 범위 지정**: `@src/` 폴더 전체를 컨텍스트로 넘김
- **스캐폴딩 요청**: 기본 구조 생성 후 내가 채움
- **디버깅 요청**: Traceback 전체를 붙여넣고 원인→수정 패치 요청

## 4. 오늘의 워크플로: 프로젝트 세팅

### 폴더 구조
```
project_w3/
├── src/
│   ├── hello_pipeline.py
│   └── utils.py
├── tests/
├── data/
│   └── sample/
├── docs/
├── .venv/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### venv 세팅 순서
1. `python -m venv .venv`
2. `source .venv/bin/activate` (Mac/Linux)
3. `pip install -r requirements.txt`
4. Cursor 인터프리터를 `.venv`로 지정

### requirements.txt (핀 버전)
```
pandas==2.2.1
numpy==1.26.4
python-dotenv==1.0.1
openai==1.30.0
anthropic==0.28.0
```

## 5. 디버깅 루틴

1. **재현** — 버그를 최소 입력으로 줄인다
2. **복사** — Traceback 전체를 Cursor Agent에 붙여넣는다
3. **diff 읽기** — 패치 적용 전에 변경사항을 확인한다
4. **logging** — `print` 대신 `logging.debug()` 사용

## 6. 오늘의 배움

- Cursor Tab은 import/예외처리를 한 줄씩 검토하며 수락해야 실수가 없다
- @멘션으로 파일 범위를 제한하면 엉뚱한 파일을 건드리지 않는다
- 작은 커밋이 디버깅 시 roll-back 비용을 크게 낮춘다

## 참고
- [Cursor 공식 문서](https://cursor.sh/docs)
- 프로젝트 레포: `project_w3/`
- 다음 날(W3D2): GA4 데이터 분석 스크립트 작성
