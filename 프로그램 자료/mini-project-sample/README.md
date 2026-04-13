# 미니 프로젝트 풀 패키지 — **서비스 리뷰·VOC AI 분석 대시보드**

> **선정 주제 (§4 후보 중 ①):** 앱 스토어·플레이 스토어 등 **서비스 리뷰·VOC**를 수집·분류(감성·토픽)하고 **Looker Studio / 웹 대시보드**로 시각화하는 **개인 미니 프로젝트** 예시입니다.  
> 본 폴더는 **교육용 샘플**: `python` + 키워드 규칙으로 LLM 없이 동일 **산출물 형식**을 재현합니다. (실제 과제는 인턴이 데이터·파이프라인·시각화를 **개인별**로 설계·구현합니다.)

---

## 빠른 실행

```bash
cd mini-project-sample
python3 collect_raw.py   # data/sample_voc_reviews.csv → data/raw.csv
python3 pipeline.py      # output/report.json, output/insights_weekly.md, 로그 append
```

- Python **3.9+**, **추가 pip 불필요** (`requirements.txt` 참고).
- 실제 제출 시: 리뷰 수집·**Claude API** 감성·토픽 분류·**Spring Boot** 배치·**Next.js** 대시보드 등 계획서 스택으로 확장합니다.

---

## 이 주제에서 나와야 하는 산출물 (전체)

| 구분 | 산출물 | 경로 |
|------|--------|------|
| 환경 | 의존성·예시·무시 규칙 | `requirements.txt`, `.env.example`, `.gitignore` |
| 기획 | 기획서·범위 정의 | `docs/md/mini_project_plan.md`, `docs/md/mini_project_scope.md` |
| 데이터 | 출처·수집 정책 | `docs/md/data_sources.md` |
| 벤치마크 | 유사 대시보드·서비스 리서치 | `docs/md/benchmark_policy_w5.md` |
| 원천 데이터 | VOC 샘플 CSV (복사본) | `data/sample_voc_reviews.csv` → `data/raw.csv` |
| 파이프라인 | 수집·라벨링 | `collect_raw.py`, `pipeline.py` |
| 분석 결과 | JSON 스키마·건건별 라벨 | `output/report.json` |
| 브리핑 | 주간 VOC 인사이트 MD | `output/md/insights_weekly.md` |
| 로그 | 실행 이력 | `output/pipeline_run.log` |
| 검증 | 사람 라벨 vs 모델 비교 | `docs/md/validation_w6.md` |
| 시각화 | 대시보드 설명·HTML 미리보기 | `docs/md/dashboard_note.md`, `viz/dashboard_preview.html` |
| 중간 | 데모 스크립트·중간 점검·진행·자동화 메모 | `docs/md/demo_script_w6.md`, `docs/md/mid_review_w6.md`, `docs/md/progress_w6.md`, `docs/md/automation_doc_w6.md` |
| 발표 | 최종 발표 아웃라인 | `docs/md/presentation_outline_w7.md` |

**PPT**는 본 패키지에 없고 `presentation_outline_w7.md`를 복사해 제작합니다.

---

## 디렉터리 구조

```
mini-project-sample/
├── README.md
├── word/README.docx
├── requirements.txt
├── .env.example
├── .gitignore
├── collect_raw.py
├── pipeline.py
├── data/
│   ├── sample_voc_reviews.csv
│   └── raw.csv                 ← collect_raw 실행 후
├── output/
│   ├── report.json
│   ├── md/insights_weekly.md
│   ├── word/insights_weekly.docx
│   └── pipeline_run.log
├── docs/
│   ├── md/          ← Markdown 산출물
│   └── word/        ← Word 내보내기
└── viz/
    └── dashboard_preview.html
```

---

## 실패 시 확인

| 증상 | 조치 |
|------|------|
| `data/raw.csv 없음` | `python3 collect_raw.py` 먼저 실행 |
| JSON·MD가 예전 주제 | `python3 pipeline.py` 재실행 |

---

*멘토와 합의한 파일명·스토어 계정·수집 범위에 맞춰 복사·수정해 사용하세요.*
