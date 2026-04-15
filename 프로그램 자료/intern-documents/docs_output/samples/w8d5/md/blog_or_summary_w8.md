# 인턴십 후기 & 기술 노트 — W8D5

**날짜:** 2026-06-05 (금)
**일정:** W8D5 — 수료·GitHub·블로그·감사·마무리 면담
**작성자:** 인턴
**용도:** 블로그 포스팅 또는 포트폴리오 요약 (공개 가능한 내용만)

---

## 인턴십 한 줄 소개

> "8주 동안 공공기관 AI 현황 387건을 자동 분류하는 파이프라인을 혼자 기획·구현·발표했다."

---

## 트러블슈팅 노트 (기술 공개용)

### 문제: LLM 분류 결과 JSON 파싱 실패

**상황:** gpt-4o-mini가 간헐적으로 JSON이 아닌 마크다운 코드블록으로 응답을 반환해 `json.loads()` 에러 발생.

**시도한 것:**
1. 프롬프트에 "반드시 JSON만 반환" 명시 → 개선됐으나 완전 해결 안 됨
2. 응답에서 JSON 부분만 정규식으로 추출 → 성공률 향상

**최종 해결:**
```python
import re, json

def safe_parse(llm_response):
    # JSON 블록 추출 시도
    match = re.search(r'\{.*\}', llm_response, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass
    return {"category": "UNKNOWN", "confidence": 0.0}
```

**배운 점:** LLM 출력은 항상 방어적으로 파싱해야 한다. temperature=0으로 고정해도 포맷 불일치는 발생한다.

---

## 도구 사용 팁 (공개용)

### Claude Cowork 보고서 생성 프롬프트 패턴
```
[규칙]
- 수치는 첨부 파일에서 직접 가져올 것
- 환각 의심 문장에는 [확인 필요] 태그 부착
- 한국어, 임원용 톤, 500자 이내
```

### Cursor Agent 효율 팁
- `@파일명`으로 컨텍스트를 명시적으로 지정
- 변경 전 항상 diff 미리 보기
- 한 번에 하나의 기능만 요청

---

## GitHub 저장소 공개 범위

| 포함 | 미포함 |
|------|--------|
| src/ (파이프라인 코드) | data/raw/ (원본 수집 데이터) |
| data/sample/ (합성 샘플) | .env (API 키) |
| tests/ | output/ (실행 결과) |
| docs/ | 멘토 피드백 원문 |
| README.md, LICENSE | — |

## 참고
- 마무리 메모: `closing_notes_w8.md`
- 회고 보고서: `w8d3/md/reflection_report_final.md`
