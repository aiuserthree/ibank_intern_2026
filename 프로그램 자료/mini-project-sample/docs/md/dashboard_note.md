# 시각화 메모 — **VOC AI 분석 대시보드**

**도구:** Looker Studio(계획서 권미정 담당) 또는 `viz/dashboard_preview.html` 정적 미리보기 · **윤서연** Next.js 프론트 연동 시 동일 지표.

## 지표 정의

| 지표 | 정의 | 소스 |
|------|------|------|
| VOC 토픽 분포 | `report.json`의 `items[].voc_topic` 건수 | 파이프라인 |
| 감성 분포 | `items[].sentiment` (긍정/부정/중립) | 파이프라인 |
| 평점 분포(선택) | `rating` 히스토그램 | 원천 CSV |
| 채널별(선택) | `source_type` 필터 | 원천 CSV |

## 캡션 예시

> 그림 1. 샘플 7건 기준 VOC 토픽 분포. 실제 운영 시 기간·앱·스토어 필터를 적용합니다.

## 파일

- 정적 미리보기: `viz/dashboard_preview.html` (토픽·감성 2블록)  
- Looker 연동 시: `report.json` 또는 BigQuery 적재 후 동일 지표 정의  
