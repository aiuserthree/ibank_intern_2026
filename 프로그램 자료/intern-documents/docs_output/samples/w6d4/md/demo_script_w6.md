# 데모 스크립트 — W6D4

**날짜:** 2026-05-21 (목)
**일정:** W6D4 — 중간 점검 — 데모·피드백 반영
**작성자:** 인턴
**데모 시간:** 5분 이내

---

## 데모 준비 체크리스트

- [x] 입력 파일 고정: `data/sample/demo_input_10.jsonl` (10건)
- [x] 클린 터미널 열기
- [x] .env 환경변수 로드 확인
- [x] 예상 출력 미리 확인: `output/expected_demo.json`

---

## 1단계: 환경 확인 (30초)

```bash
# 터미널에서 복사-붙여넣기
cd project_mini
source .venv/bin/activate
python --version  # 3.12.x 확인
python -c "import openai; print('API 연결 OK')"
```

**예상 출력:**
```
Python 3.12.3
API 연결 OK
```

---

## 2단계: 파이프라인 실행 (1분 30초)

```bash
python run.py   --input data/sample/demo_input_10.jsonl   --out output/demo_result.json   --verbose
```

**예상 출력:**
```
[INFO] 10건 로드 완료
[INFO] 전처리 완료: 10건
[INFO] LLM 분류 시작...
[INFO] 배치 1/1 완료 (10건)
[SUCCESS] output/demo_result.json 저장 완료
처리 시간: 13.4초
```

---

## 3단계: 결과 확인 (1분)

```bash
python -c "
import json
with open('output/demo_result.json') as f:
    results = json.load(f)
for r in results[:3]:
    print(f"{r['doc_id']}: {r['category']} ({r['confidence']:.2f})")
"
```

**예상 출력:**
```
doc_d01: 민원·행정 자동화 (0.94)
doc_d02: 의료·복지 AI (0.88)
doc_d03: 데이터 분석·예측 (0.91)
```

---

## 4단계: 분포 요약 (30초)

```bash
python -c "
import json, collections
with open('output/demo_result.json') as f:
    results = json.load(f)
counts = collections.Counter(r['category'] for r in results)
for cat, cnt in counts.most_common():
    print(f'{cat}: {cnt}건')
"
```

---

## 멘토 예상 질문 & 답변 메모

| 예상 질문 | 준비된 답변 |
|-----------|------------|
| 정확도는 얼마나 되나요? | 현재 82%, 목표 85% — 프롬프트 v0.3 테스트 중 |
| 500건은 언제 완료되나요? | 현재 387건, W6D4~D5 내 완료 예정 |
| 재현이 가능한가요? | 동일 커맨드로 동일 결과, temperature=0 고정 |
| 비용은? | 건당 약 $0.0004, 500건 기준 약 $0.20 |
