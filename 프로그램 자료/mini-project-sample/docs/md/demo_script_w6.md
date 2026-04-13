# 데모 스크립트 — **VOC 파이프라인** (6주차 중간 점검용)

**길이:** 약 5~7분 · **산출:** `report.json` + `insights_weekly.md` + 대시보드 HTML

## 사전 준비

- [ ] Python 3.9+
- [ ] `data/raw.csv` 존재 (`python3 collect_raw.py`)

## 진행

1. **문제 (30초)**  
   - 스토어 리뷰가 많아져 **VOC 토픽·감성**을 자동 태깅하고 대시보드에 올리는 게 목표.

2. **데이터 (1분)**  
   - `sample_voc_reviews.csv` → `raw.csv` — 가상 앱명·평점·리뷰 텍스트(교육용).

3. **실행 (2분)**  
   ```bash
   python3 collect_raw.py
   python3 pipeline.py
   ```
   - `output/report.json`: `voc_topic`, `sentiment`, `rating` 필드 확인.

4. **인사이트 (1.5분)**  
   - `output/insights_weekly.md` — 토픽·감성 표.  
   - `viz/dashboard_preview.html` — 막대 차트 2종.

5. **한계 (30초)**  
   - 샘플은 규칙 기반 → 실제는 **Claude API**·검수.

## 실패 시

- `raw.csv` 없음 → `collect_raw.py` 먼저 안내.
