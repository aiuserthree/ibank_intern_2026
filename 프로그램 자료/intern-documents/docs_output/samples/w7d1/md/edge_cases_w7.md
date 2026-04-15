# 엣지 케이스 목록 & 예외 처리 — W7D1

**날짜:** 2026-05-25 (월)
**일정:** W7D1 — 기능 완성 & 엣지 케이스
**작성자:** 인턴

---

## 1. 엣지 케이스 목록 (수집 모듈)

| ID | 입력 유형 | 재현 방법 | 기대 동작 | 우선순위 |
|----|----------|----------|----------|---------|
| E-01 | 빈 입력 파일 (0바이트) | `echo "" > test.jsonl` | 빈 리스트 반환 + 경고 로그 | Must |
| E-02 | 깨진 인코딩 (EUC-KR) | EUC-KR 파일 입력 | UTF-8 강제 변환 시도 후 실패 시 skip | Must |
| E-03 | 대용량 단일 문서 (>10,000자) | 1만자 텍스트 파일 | 청크 분할 후 각 청크 처리 | Must |
| E-04 | 특수문자 다수 (이모지·HTML 태그) | `<b>테스트</b>🎯` | 정규화 후 순수 텍스트 추출 | Should |
| E-05 | 중복 doc_id | 동일 ID 2개 포함 | 첫 번째만 처리 + 중복 경고 | Should |
| E-06 | API 연결 실패 | 네트워크 차단 상태 | 3회 재시도 후 오류 로그 + 종료 | Must |
| E-07 | 분류 결과 JSON 파싱 실패 | 프롬프트 응답이 비JSON | UNKNOWN 처리 + 재시도 1회 | Must |
| E-08 | 0건 수집 결과 | RSS 피드 빈 응답 | 경고 로그 + 빈 CSV 출력 | Should |

---

## 2. 예외 처리 코드 패턴

### 수집 모듈 (collect_raw.py)
```python
try:
    raw = fetch_from_api(url, timeout=10)
except requests.exceptions.Timeout:
    logger.warning(f"[TIMEOUT] {url} — 3회 재시도 예정")
    raw = retry_fetch(url, max_retries=3)
except requests.exceptions.ConnectionError:
    logger.error(f"[CONN_ERR] {url} — 네트워크 확인 필요")
    raise
```

### 분류 모듈 (classify.py)
```python
try:
    result = json.loads(llm_response)
except json.JSONDecodeError:
    logger.warning(f"[JSON_ERR] doc_id={doc_id} — UNKNOWN 처리")
    result = {"category": "UNKNOWN", "confidence": 0.0}
```

---

## 3. 로그 레벨 정책

| 레벨 | 사용 상황 | 예시 |
|------|----------|------|
| DEBUG | 개발 중 상세 추적 | 배치 처리 중간 상태 |
| INFO | 정상 진행 이정표 | "50건 처리 완료" |
| WARNING | 비정상이지만 계속 가능 | 중복 ID, 신뢰도 낮음 |
| ERROR | 처리 중단 필요 | API 연결 실패 |

---

## 4. 처리 결과

| 케이스 | 수정 완료 | 관련 이슈 |
|--------|----------|----------|
| E-01 빈 입력 | ✅ | — |
| E-02 인코딩 | ✅ | — |
| E-03 대용량 | ✅ | — |
| E-06 API 실패 | ✅ | — |
| E-07 JSON 파싱 | ✅ | — |
| E-04 특수문자 | 🔄 진행 중 | #8 |
| E-05 중복 ID | ⬜ 예정 | #9 |
| E-08 0건 결과 | ⬜ 예정 | #10 |

## 참고
- 회귀 테스트: `regression_w7.md`
- 관련 이슈: GitHub #8~10
