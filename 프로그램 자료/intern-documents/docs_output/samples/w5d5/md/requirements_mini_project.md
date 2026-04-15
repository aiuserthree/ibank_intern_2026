# 미니 프로젝트 요구사항 정의서 — W5D5

**날짜:** 2026-05-15 (금)
**일정:** W5D5 — 미니 프로젝트 기획서 & 주간 정리
**작성자:** 인턴

---

## 1. 기능 요구사항 (Functional)

| ID | 요구사항 | 우선순위 | 담당 주차 |
|----|---------|---------|----------|
| F-01 | 공공 텍스트 500건 수집 및 저장 | Must | W5~W6 |
| F-02 | 5개 분야 LLM 분류 (정확도 ≥ 85%) | Must | W6 |
| F-03 | 월별 트렌드 시각화 (Looker Studio) | Must | W7 |
| F-04 | 정책 인사이트 보고서 (2,000자) | Must | W7 |
| F-05 | 실패 문서 재처리 기능 | Should | W6 |
| F-06 | 분류 결과 CSV 내보내기 | Should | W6 |
| F-07 | 자동화 스케줄러 연결 | Could | W8 |

---

## 2. 비기능 요구사항 (Non-Functional)

| ID | 요구사항 | 기준 |
|----|---------|------|
| NF-01 | 재현성 | 동일 입력 → 동일 출력 (temperature=0) |
| NF-02 | 보안 | API 키 환경변수 관리 (.env) |
| NF-03 | 성능 | 100건 처리 ≤ 5분 |
| NF-04 | 문서화 | 모든 함수에 docstring |

---

## 3. 시스템 구성

```
project_mini/
├── src/
│   ├── collect_raw.py      # 데이터 수집
│   ├── preprocess.py       # 텍스트 정제
│   ├── classify.py         # LLM 분류
│   └── visualize.py        # 결과 시각화
├── data/
│   ├── raw/                # 원본 수집 데이터
│   ├── processed/          # 정제 데이터
│   └── gold/               # 평가 골드셋
├── output/
│   ├── report.json         # 분류 결과
│   └── dashboard_data.csv  # 시각화용 데이터
├── requirements.txt
├── .env.example
└── README.md
```

---

## 4. 인터페이스 정의

### 입력
```
python src/classify.py   --input data/processed/texts.jsonl   --model gpt-4o-mini   --out output/report.json
```

### 출력 (report.json)
```json
{
  "doc_id": "doc_001",
  "title": "민원24 AI 자동분류 도입",
  "category": "민원·행정 자동화",
  "confidence": 0.95,
  "pub_date": "2025-08-15",
  "source": "행정안전부"
}
```

---

## 5. 의존성

| 패키지 | 버전 | 용도 |
|--------|------|------|
| openai | 1.30.0 | LLM API |
| anthropic | 0.28.0 | Claude API |
| pandas | 2.2.1 | 데이터 처리 |
| feedparser | 6.0.11 | RSS 수집 |
| pdfplumber | 0.11.0 | PDF 텍스트 추출 |
| python-dotenv | 1.0.1 | 환경변수 |

---

## 참고
- 기획서: `mini_project_plan_w5.md`
- 파이프라인 결과: `w5d2/md/report.json.md`
