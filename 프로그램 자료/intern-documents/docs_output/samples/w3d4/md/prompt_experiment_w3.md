# 프롬프트 실험 기록 — W3D4

**날짜:** 2026-04-30 (목)  
**일정:** W3D4 — 프롬프트 심화 — Few-shot & Chain-of-Thought  
**작성자:** 인턴  
**상태:** 작성 완료

---

## 1. Few-shot 실험

### 실험 목적
Few-shot 예시 수(0~4개)가 분류 정확도에 미치는 영향 측정

### 실험 조건
- **모델**: gpt-4o-mini, temperature=0
- **태스크**: 뉴스 헤드라인 감성 분류 (POSITIVE / NEGATIVE / NEUTRAL)
- **테스트셋**: 수동 라벨 50건

### 결과 비교표

| 예시 수 | 정확도 | 형식 준수율 | 비고 |
|---------|--------|-------------|------|
| 0-shot  | 72%    | 85%         | JSON 형식 오류 많음 |
| 1-shot  | 80%    | 92%         | 경계 케이스 혼동 |
| 2-shot  | 86%    | 97%         | 균형 잡힌 성능 |
| 4-shot  | 88%    | 98%         | 토큰 비용 2배 |

**결론**: 2-shot이 비용 대비 최적. 4-shot은 정확도 향상 폭이 작아 비효율.

---

## 2. Chain-of-Thought 실험

### CoT 프롬프트 추가 문구
```
단계별로 생각한 뒤 최종 결론을 JSON으로 출력하세요.
1) 텍스트의 핵심 감정 신호 단어를 찾는다
2) 긍정/부정/중립 여부를 판단한다
3) 확신도를 0~1로 추정한다
```

### CoT on/off 비교

| 케이스 | CoT OFF | CoT ON |
|--------|---------|--------|
| "주가가 급락했습니다" | NEGATIVE (0.9) ✅ | NEGATIVE (0.93) ✅ |
| "대형 인수합병 완료" | POSITIVE (0.7) ✅ | POSITIVE (0.85) ✅ |
| "시장이 반응하지 않았다" | POSITIVE (0.6) ❌ | NEUTRAL (0.78) ✅ |
| "기대 이하의 실적" | NEGATIVE (0.8) ✅ | NEGATIVE (0.91) ✅ |
| "업계 표준에 부합" | NEUTRAL (0.5) ✅ | NEUTRAL (0.82) ✅ |

**결론**: CoT는 모호한 경계 케이스에서 특히 효과적. 명확한 케이스는 속도가 느려져 선택적 적용 권장.

---

## 3. Self-Consistency 결과

### 설정
- temperature = 0.7, n = 5회 반복
- 대상: 경계 케이스 10건

### 분석
- 5/5 일치: 7건 → 안정적
- 3/5~4/5 일치: 2건 → 재검토 필요
- 2/5 이하 일치: 1건 → 프롬프트 수정 대상

**비용 고려**: n=5 호출 시 비용 5배 증가 → 신뢰도 요구가 높은 태스크에만 적용

---

## 4. 실험 재현 커맨드

```bash
# Few-shot 실험 재현
python experiments/few_shot_exp.py   --shots 0 1 2 4   --test-data data/gold_50.csv   --out results/few_shot_results.csv

# CoT 실험 재현
python experiments/cot_exp.py   --mode compare   --test-data data/gold_50.csv   --out results/cot_results.csv
```

## 참고
- 프롬프트 버전 파일: `prompt_library_v2.md`
- 정확도 비교 표: `accuracy_comparison.md`
- 실험 스크립트: `experiments/`
