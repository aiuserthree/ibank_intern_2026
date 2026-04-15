# API 사용 노트 — W3D3

**날짜:** 2026-04-29 (수)  
**일정:** W3D3 — OpenAI / Claude API — 분류·요약 파이프라인  
**작성자:** 인턴  
**상태:** 작성 완료

---

## 1. 환경 설정

### .env.example
```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
MODEL_OPENAI=gpt-4o-mini
MODEL_CLAUDE=claude-haiku-4-5-20251001
```

### 클라이언트 초기화 패턴

**OpenAI (Chat Completions)**
```python
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "텍스트를 분류해줘"}],
    max_tokens=256
)
print(response.choices[0].message.content)
```

**Anthropic (Messages API)**
```python
import anthropic

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=256,
    messages=[{"role": "user", "content": "텍스트를 분류해줘"}]
)
print(message.content[0].text)
```

---

## 2. 분류 파이프라인 설계

### 프롬프트 구조 (Few-shot)
```
당신은 텍스트 분류 전문가입니다.
아래 카테고리 중 하나로 분류하고 JSON으로만 응답하세요.

카테고리:
- POSITIVE: 긍정적 내용
- NEGATIVE: 부정적 내용
- NEUTRAL: 중립적 내용

예시:
입력: "오늘 점심이 너무 맛있었어요"
출력: {"label": "POSITIVE", "confidence": 0.95}

입력: "서비스가 별로였습니다"
출력: {"label": "NEGATIVE", "confidence": 0.90}

분류할 텍스트: {text}
```

### JSON 파싱 코드
```python
import json, re

def parse_label(response_text):
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        # 정규식 fallback
        match = re.search(r'\{.*?\}', response_text, re.DOTALL)
        if match:
            return json.loads(match.group())
        return {"label": "UNKNOWN", "confidence": 0.0}
```

---

## 3. 배치 처리 & 비용 추산

### 배치 설정
| 항목 | 설정값 | 이유 |
|------|--------|------|
| 배치 크기 | 10건 | 토큰 한도 여유 확보 |
| 재시도 횟수 | 3회 | 429/5xx 대응 |
| 백오프 | 2^n 초 | 지수 증가 |
| 캐시 | SHA-256 해시 | 중복 호출 방지 |

### 비용 추산 (gpt-4o-mini 기준)
| 항목 | 수치 |
|------|------|
| 건당 평균 토큰 | 입력 200 + 출력 50 = 250 tokens |
| 1,000건 비용 | 약 $0.04 (input $0.15/1M, output $0.60/1M) |
| 일 1만 건 처리 | 약 $0.40 |

---

## 4. 품질 평가 결과

### 테스트셋 (50건 수동 라벨)
| 모델 | 정확도 | 오류 유형 |
|------|--------|-----------|
| gpt-4o-mini | 88% | 경계 케이스 혼동 |
| claude-haiku | 86% | 형식 오류 (JSON 미반환 2%) |

### 주요 오류 유형
1. **환각**: 존재하지 않는 카테고리 응답 → 유효성 검사로 차단
2. **분류 혼동**: NEUTRAL ↔ POSITIVE 경계 → 예시 추가로 개선
3. **형식 오류**: JSON 대신 자연어 응답 → `response_format={"type":"json_object"}` 사용

---

## 5. 통합 실행 방법

```bash
# 기본 실행
python run_pipeline.py --input data/sample/texts.csv --out output/

# 옵션
python run_pipeline.py   --input data/sample/texts.csv   --out output/   --model gpt-4o-mini   --batch-size 10   --cache
```

### 출력 파일
- `output/classified.csv`: label, confidence, 원본 텍스트
- `output/summary.json`: 전체 통계 (총 건수, 클래스별 비율, 평균 신뢰도)

---

## 6. 학습 정리

- JSON mode로 응답 형식을 강제하면 파싱 오류가 크게 줄어든다
- 배치 크기 10이 비용·속도 트레이드오프에서 최적이었다
- 캐시를 넣으면 개발 중 반복 테스트 비용을 90% 절감 가능

## 참고
- [OpenAI API 문서](https://platform.openai.com/docs)
- [Anthropic API 문서](https://docs.anthropic.com)
- 스크립트: `src/api_classify.py`, `src/api_summarize.py`
