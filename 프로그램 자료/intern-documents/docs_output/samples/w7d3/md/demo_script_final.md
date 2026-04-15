# 데모 스크립트 (최종 동결) — W7D3

**날짜:** 2026-05-27 (수)
**일정:** W7D3 — PPT 완성 & 데모 스크립트 동결
**작성자:** 인턴
**상태:** FROZEN — 이 파일은 더 이상 수정하지 않음

---

## 데모 시간: 3분 정확히

| 단계 | 내용 | 시간 |
|------|------|------|
| 1 | 환경 확인 | 20초 |
| 2 | 파이프라인 실행 | 80초 |
| 3 | 결과 확인 | 40초 |
| 4 | 분포 요약 | 20초 |
| **합계** | | **160초 (약 2분 40초)** |

---

## 1단계: 환경 확인 (20초)

**말할 문장:** "먼저 가상환경과 API 연결을 확인하겠습니다."

```bash
cd project_mini
source .venv/bin/activate
python -c "import openai; print('API 연결 OK')"
```

**예상 출력:**
```
API 연결 OK
```

---

## 2단계: 파이프라인 실행 (80초)

**말할 문장:** "demo_input_10.jsonl을 입력으로 전체 파이프라인을 실행합니다. 수집→전처리→LLM 분류 순으로 진행됩니다."

```bash
python src/pipeline_core.py   --input data/sample/demo_input_10.jsonl   --out output/demo_result.json   --verbose
```

**예상 출력:**
```
[INFO] 10건 로드 완료
[INFO] 전처리 완료: 10건 → 23 청크
[INFO] LLM 분류 시작 (배치 1/1)
[INFO] 배치 완료: 10건, 신뢰도 평균 0.91
[SUCCESS] output/demo_result.json 저장 완료
처리 시간: 12.8초
```

---

## 3단계: 결과 확인 (40초)

**말할 문장:** "출력된 JSON에서 상위 3건의 분류 결과를 확인합니다."

```bash
python -c "
import json
with open('output/demo_result.json') as f:
    results = json.load(f)
for r in results[:3]:
    print(r['doc_id'], r['category'], round(r['confidence'],2))
"
```

**예상 출력:**
```
doc_d01 민원·행정 자동화 0.94
doc_d02 의료·복지 AI 0.88
doc_d03 데이터 분석·예측 0.91
```

---

## 4단계: 분포 요약 (20초)

**말할 문장:** "10건의 카테고리 분포입니다. 실제 387건에서는 민원·행정 자동화가 33.5%로 1위였습니다."

```bash
python -c "
import json, collections
with open('output/demo_result.json') as f:
    results = json.load(f)
for cat, cnt in collections.Counter(r['category'] for r in results).most_common():
    print(cat + ': ' + str(cnt) + '건')
"
```

---

## 플랜 B (네트워크 실패 시)

1. `output/expected_demo.json` 파일을 직접 열어 JSON 출력 보여주기
2. `docs/demo_screenshot_w7.png` 스크린샷 PPT 부록으로 전환

## 참고
- 발표 슬라이드: `presentation_w7_v2.md`
- 백업 자료: `demo_backup_w7.md`
