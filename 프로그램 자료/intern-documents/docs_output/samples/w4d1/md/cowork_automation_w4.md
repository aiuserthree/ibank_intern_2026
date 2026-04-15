# Claude Cowork AI 업무 자동화 실습 — W4D1

**날짜:** 2026-05-04 (월)  
**일정:** W4D1 — Claude Cowork — AI 업무 자동화 실습  
**작성자:** 인턴  
**상태:** 작성 완료

---

## 1. 자동화 후보 선정

반복되는 업무 5개를 추출하고 빈도×시간으로 우선순위를 계산했습니다.

| 업무 | 빈도 | 수동 소요 | 월 총 소요 | 자동화 난이도 |
|------|------|-----------|------------|---------------|
| 주간 현황 리포트 작성 | 주 1회 | 45분 | 3.0시간 | 2/5 |
| 수신 이메일 분류·답장 초안 | 일 3회 | 10분 | 4.0시간 | 3/5 |
| 파일 이름 정리·이동 | 주 2회 | 20분 | 2.7시간 | 1/5 |
| 뉴스 클리핑 요약 | 일 1회 | 30분 | 9.0시간 | 2/5 |
| 회의록 작성 | 주 3회 | 25분 | 5.0시간 | 3/5 |

**선택된 상위 2개:** ① 뉴스 클리핑 요약 (월 9h), ② 주간 리포트 작성 (월 3h)

---

## 2. Cowork 절차 문서화

### 뉴스 클리핑 자동화 절차
1. RSS 피드 또는 키워드 목록을 `config/news_keywords.json`에 저장
2. 스크립트가 매일 07:00 뉴스를 수집 (`src/fetch_news.py`)
3. 수집된 제목·URL을 Cowork에 전달
4. Cowork가 각 기사를 2~3줄로 요약
5. 결과를 `reports/news_YYYY-MM-DD.md`에 저장

### 위험 단계 (수동 유지)
- ⚠️ 최종 외부 발송 전 내용 검토 (법무·컴플라이언스)
- ⚠️ PII 포함 파일 처리 시 별도 승인 필요

---

## 3. 스크립트 스텁 구조

```python
# src/news_automation.py (stub)
import os, logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

INPUT_DIR = Path("data/news_raw")
OUTPUT_DIR = Path("reports")

def process_batch(files):
    for f in files:
        logging.info(f"Processing: {f.name}")
        # TODO: Cowork 요약 API 호출
        OUTPUT_DIR.mkdir(exist_ok=True)

if __name__ == "__main__":
    files = list(INPUT_DIR.glob("*.txt"))
    logging.info(f"Found {len(files)} files")
    process_batch(files)
```

---

## 4. 오류 처리 & 알림

| 오류 유형 | 처리 방법 |
|-----------|-----------|
| API 타임아웃 | 3회 재시도 후 Slack 알림 발송 |
| 파일 없음 | 건너뜀 + 로그 기록 |
| 중복 처리 | SHA-256 해시로 중복 감지 |
| 논리 오류 | 즉시 중단 + 에러 로그 저장 |

---

## 5. 오늘의 배움

- 자동화 후보 선정 시 빈도×시간이 가장 직관적인 기준
- Cowork와 연동 전 절차를 번호 목록으로 명확히 해야 AI가 맥락을 잃지 않는다
- 승인·법무 단계는 절대 자동화하면 안 됨 — 반드시 수동으로 남길 것

## 참고
- 다음 단계: `sample_briefing_w4.md` 참고
- 스크립트: `src/news_automation.py`
- 운영 가이드: `runbook_w4.md`
