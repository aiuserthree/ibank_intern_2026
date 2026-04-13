# 미니 프로젝트 범위 — **서비스 리뷰·VOC AI 분석 대시보드**

## 포함

- **데이터:** 앱 스토어·플레이 스토어 등 **공개 리뷰** (샘플은 `sample_voc_reviews.csv` 가공 데이터).  
- **분석:** 리뷰 텍스트별 **VOC 토픽**(예: 성능·버그·UX·가격·고객지원 등) + **감성**(긍정/부정/중립).  
- **산출:** `report.json`, 주간 `insights_weekly.md`, **대시보드**(정적 HTML 또는 Looker·Next.js).  
- **연계:** 실제 서비스에서는 **Spring Boot**·**Claude API**·**Next.js** 등 계획서 스택으로 확장.

## 제외

- 사내 비공개 VOC 원문 전량(권한 없이).  
- 리뷰어 개인 식별·재배포 금지 조항 위반.  
- 무차별 스크래핑·API 약관 위반 수집.

## 성공 기준

- `python collect_raw.py` → `python pipeline.py` 가 오류 없이 끝남.  
- `output/report.json`의 `meta.project`·`items[].voc_topic` 스키마가 문서와 일치.  
- 대시보드에서 **토픽·감성 분포**를 동일 숫자로 확인 가능.

## 개인 수행 범위

- 인턴 본인이 데이터·파이프라인·시각화·문서화·발표를 **통합**해 담당합니다. (필요 시 멘토와 단계별 범위 조정)
