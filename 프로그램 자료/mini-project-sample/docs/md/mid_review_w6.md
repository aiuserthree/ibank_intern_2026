# 중간 점검 메모 — **VOC AI 분석 대시보드**

- **일시:** (멘토 일정에 맞춤)  
- **참석:** 멘토 조준형 · 인턴 권미정·박수빈·윤서연  

## 결정

- 주제: **서비스 리뷰·VOC AI 분석 대시보드** (§4 후보 ①) 유지.  
- 스키마: `voc_topic` + `sentiment` + `rating` + `review_excerpt`.  
- 차주: Looker 또는 Next.js에 동일 지표 연결.

## 미해결

- 실제 스토어 수집 시 **일일 쿼터**·저장 주기.  
- LLM 비용 대비 **배치 크기**.

## 다음 액션

1. `validation_w6.md`에 사람 라벨 10건 추가.  
2. 대시보드 `dashboard_preview.html`과 `report.json` 건수 동기화 확인.  
