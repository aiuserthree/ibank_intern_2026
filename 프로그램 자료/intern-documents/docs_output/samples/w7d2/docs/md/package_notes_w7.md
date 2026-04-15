# 산출물 패키징 노트 — W7D2

**날짜:** 2026-05-26 (화)
**일정:** W7D2 — 산출물 패키징 — README·폴더·라이선스
**작성자:** 인턴

---

## 1. 디렉터리 구조

```
project_mini/
├── src/
│   ├── collect_raw.py      # 공공 API·RSS 수집
│   ├── preprocess.py       # 텍스트 정제·청킹
│   ├── classify.py         # LLM 분류 배치
│   ├── pipeline_core.py    # 전체 파이프라인 실행
│   └── visualize.py        # 차트 생성
├── data/
│   └── sample/
│       ├── demo_input_10.jsonl   # 데모용 10건 샘플
│       └── README.md
├── docs/
│   ├── package_notes_w7.md
│   └── architecture.md
├── output/                 # 실행 결과 (gitignore)
├── tests/
│   ├── test_collect.py
│   ├── test_preprocess.py
│   └── test_classify.py
├── scripts/
│   └── generate_sample.py  # 합성 샘플 생성 스크립트
├── .env.example
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 2. README 5분 완성 체크리스트

| 항목 | 완료 | 내용 |
|------|------|------|
| 프로젝트 한 줄 설명 | ✅ | "공공기관 AI 도입 현황 자동 분류·분석 파이프라인" |
| 환경 설정 (venv + pip) | ✅ | python -m venv .venv && pip install -r requirements.txt |
| 실행 한 줄 | ✅ | python src/pipeline_core.py --input data/sample/demo_input_10.jsonl |
| 자주 나는 에러 2개 | ✅ | API 키 없음, 인코딩 오류 |
| 연락처 | ✅ | GitHub Issues |

---

## 3. 샘플 데이터 생성 방법

```bash
# 합성 샘플 10건 생성
python scripts/generate_sample.py --n 10 --out data/sample/demo_input_10.jsonl
```

- 실제 데이터와 동일한 스키마 (doc_id, title, text, pub_date, source)
- 이름·기관명은 가상으로 치환
- 용량: 약 15KB

---

## 4. 릴리스 태그

```bash
git tag -a v1.0 -m "W7D2 패키징 완료 — 데모 가능한 상태"
git push origin v1.0
```

**v1.0 포함 항목:**
- 핵심 파이프라인 (수집·전처리·분류)
- 단위 테스트 11/13 통과
- 샘플 데이터 및 README

**v1.0 미포함 항목 (v1.1 예정):**
- E-04, E-05 엣지 케이스 수정
- 시각화 모듈 완성

## 참고
- 라이선스: `LICENSE.md`
- 샘플 데이터: `data/sample/README.md`
