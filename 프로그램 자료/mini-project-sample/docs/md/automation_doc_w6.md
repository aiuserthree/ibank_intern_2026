# Cowork·오픈클로 자동화 메모 — **VOC 리포트**

**프로젝트:** 서비스 리뷰·VOC AI 분석 대시보드

## Cowork

- **입력:** `output/report.json` 또는 `insights_weekly.md`  
- **요청 예:** "이번 주 부정 리뷰가 많은 VOC 토픽 3개 + 임원용 3불릿"  
- **출력:** 초안 MD → 사람이 수치·인용 검증  

## 오픈클로

- **트리거:** 주간 금요일 (가정)  
- **흐름:** `git log` 또는 `report.json` 경로 → 주간 요약 → `progress_w6.md` 또는 슬랙 초안 (선택)

## 주의

- 내부 URL·API 키·실제 사용자 리뷰 전문은 절대 입력하지 않기.  
