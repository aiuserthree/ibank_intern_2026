# LLM 파이프라인 가이드 — W3D5

**날짜:** 2026-05-01 (금)  
**일정:** W3D5 — Cursor 단축키·완성 방법 문서화 & 3주차 회고  
**작성자:** 인턴  
**버전:** 1.0 (3주차 최종)

---

## 1. 파이프라인 개요

이 주간 구현한 LLM 파이프라인은 CSV 텍스트 → 분류·요약 → JSON 출력의 흐름으로 구성됩니다.

```
입력 CSV
   │
   ▼
[전처리] 날짜 정제, PII 제거, 배치 분할
   │
   ▼
[분류] API 호출 (Few-shot 2-shot, JSON mode)
   │
   ▼
[요약] 분류 결과별 3줄 요약
   │
   ▼
[후처리] 파싱 검증, 캐시 저장, 오류 로깅
   │
   ▼
출력 CSV + summary.json
```

---

## 2. 실행 방법

### 환경 설정
```bash
# 1. venv 활성화
source .venv/bin/activate

# 2. 패키지 설치
pip install -r requirements.txt

# 3. 환경 변수 설정
cp .env.example .env
# .env 파일에 API 키 입력
```

### 파이프라인 실행
```bash
# 기본 실행
python run_pipeline.py --input data/sample/texts.csv --out output/

# 상세 옵션
python run_pipeline.py \
  --input data/sample/texts.csv \
  --out output/ \
  --model gpt-4o-mini \
  --batch-size 10 \
  --cache \
  --log-level INFO
```

### 출력 예시
```json
{
  "total": 100,
  "classified": 100,
  "errors": 0,
  "distribution": {
    "POSITIVE": 42,
    "NEGATIVE": 31,
    "NEUTRAL": 27
  },
  "avg_confidence": 0.89
}
```

---

## 3. 파일 구조

```
project_w3/
├── src/
│   ├── api_classify.py      # 분류 API 호출
│   ├── api_summarize.py     # 요약 API 호출
│   └── utils.py             # 공통 유틸 (캐시, 백오프)
├── experiments/
│   ├── few_shot_exp.py      # Few-shot 실험
│   └── cot_exp.py           # CoT 실험
├── data/
│   └── sample/
│       ├── texts.csv        # 입력 샘플
│       └── gold_50.csv      # 평가용 골드셋
├── output/                  # 실행 결과 저장
├── run_pipeline.py          # 메인 실행 스크립트
├── requirements.txt
├── .env.example
└── README.md
```

---

## 4. 주요 컴포넌트

### utils.py — 캐시 & 백오프

```python
import hashlib, time, json

_cache = {}

def cached_call(fn, text, **kwargs):
    key = hashlib.sha256(text.encode()).hexdigest()
    if key in _cache:
        return _cache[key]
    for attempt in range(3):
        try:
            result = fn(text, **kwargs)
            _cache[key] = result
            return result
        except Exception as e:
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)
```

---

## 5. 한계 및 주의사항

| 항목 | 내용 |
|------|------|
| 샘플링 편향 | 골드셋 50건이 적어 도메인 편향 가능 |
| 비용 | 1만 건 처리 시 gpt-4o 기준 약 $80 |
| 캐시 휘발 | 프로세스 종료 시 캐시 소멸 → Redis 연동 권장 |
| 언어 한계 | 영어 기반 모델이므로 한국어 성능 5~10% 낮음 |

---

## 6. 다음 단계 (4주차)

- 자동화 스케줄러 적용 (매주 월요일 자동 실행)
- Redis 캐시로 교체
- 평가 골드셋 확대 (50 → 200건)
- 미니 프로젝트 주제 결정

## 참고
- API 노트: `w3d3/md/api_usage_notes.md`
- 프롬프트 라이브러리: `w3d4/md/prompt_library_v2.md`
- 실험 결과: `w3d4/md/accuracy_comparison.md`
