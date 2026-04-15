# 자동화 ROI 측정 결과 — W4D2

**날짜:** 2026-05-05 (화)
**일정:** W4D2 — 반복 업무 자동화 — 주간 리포트 초안
**작성자:** 인턴
**상태:** 측정 완료

---

## 1. 반복 업무 ROI 표

| 업무 | 수동 시간(회) | 자동화 후(회) | 빈도(주) | 주간 절감 | 월간 절감 |
|------|--------------|---------------|----------|-----------|-----------|
| 뉴스 클리핑 요약 | 30분 | 3분 | 5회 | 135분 | 9.0시간 |
| 주간 리포트 초안 | 45분 | 5분 | 1회 | 40분 | 2.7시간 |
| CSV 정제 | 25분 | 2분 | 2회 | 46분 | 3.1시간 |
| 이메일 초안 | 15분 | 2분 | 10회 | 130분 | 8.7시간 |

**합계 월간 절감: 23.5시간 (1인 기준)**

---

## 2. 시간 측정 방법

- 동일 작업을 수동 2회 / 스크립트 2회 측정 후 평균값 사용
- 스톱워치: macOS 기본 타이머 앱
- 스크립트 포함 시간: 실행 시작 → 결과 파일 저장 완료까지

### 측정 편차 및 한계
- 수동 작업 속도는 날에 따라 ±5분 편차 있음
- 스크립트 실행 시간은 API 응답 속도에 따라 ±30초 변동
- 샘플이 3~5건에 불과해 100건 배치 시 다를 수 있음

---

## 3. 주간 리포트 워크플로우 (자동화)

```python
# auto_report.py 핵심 흐름
def run_weekly_report():
    df = auto_clean("data/weekly_metrics.csv")
    summary = cowork_summarize(
        data=df.to_markdown(),
        prompt="불릿 5개, 한국어, 200자 이내, 임원용 톤"
    )
    today = datetime.date.today().isoformat()
    save_report(f"reports/week_{today}.md", summary)
    if not summary:
        summary = fill_template("templates/weekly_template.md", df)
```

---

## 4. 이메일 초안 자동화 패턴

```python
# email_draft.py
def generate_email(recipient, purpose, bullets):
    bullets_text = chr(10).join(f'- {b}' for b in bullets)
    prompt = f"수신자: {recipient}\n목적: {purpose}\n핵심 내용:\n{bullets_text}\n격식체 한국어"
    draft = cowork_generate(prompt)
    assert "안녕하세요" in draft or "드립니다" in draft
    return draft
```

---

## 5. 임원용 한 줄 스토리

> "AI 자동화 도입으로 반복 업무 4종을 월 23.5시간 단축 — 개발 투자(8시간) 대비 3주 만에 손익분기 달성."

---

## 6. 다음 단계

- 오픈클로 스케줄 트리거 연결 (W4D3)
- 이메일 초안 발송 전 사람 검토 단계 유지
- 월말에 실제 절감 시간 재측정하여 이 문서 업데이트

## 참고
- 자동화 스크립트: `auto_clean.py`, `auto_report.py`, `email_draft.py`
- 스케줄 설정: W4D3에서 오픈클로와 연결 예정
