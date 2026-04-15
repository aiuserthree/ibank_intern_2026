# Cowork·오픈클로 문서 자동화 설계 — W6D3

**날짜:** 2026-05-20 (수)
**일정:** W6D3 — Cowork·오픈클로로 문서·보고 자동화
**작성자:** 인턴

---

## 1. 자동화 아키텍처

```
[파이프라인 출력]
output/report_partial.json
        ↓
[Claude Cowork]
  → 중간 보고서 초안 생성
  → output/cowork_doc_out_w6.md
        ↓
[오픈클로 트리거]
  → 파일 감지 → Google Drive 저장
  → (선택) 이메일 발송
```

---

## 2. Cowork 설정

### 작업 폴더 경로
```
project_mini/output/  ← Cowork 접근 허용 폴더
```

### 프롬프트 템플릿 (v1.0)
```
다음 JSON 파일의 분석 결과를 읽고 주간 보고서를 작성하세요.

[규칙]
- 목차: 진행률 / 분류 분포 / 핵심 인사이트 / 다음 액션
- 환각 문장에는 [확인 필요] 태그를 붙일 것
- 한국어, 임원용 톤, 500자 이내
- 수치는 JSON에서 그대로 가져올 것

파일: output/report_partial.json
```

### 파일 핸드오프 규칙
- 출력 파일명: `cowork_doc_out_YYYYMMDD.md`
- 인코딩: UTF-8 (BOM 없음)
- 오픈클로 입력 경로: `output/cowork_doc_out_*.md`

---

## 3. 오픈클로 플로우

| 단계 | 액션 | 도구 |
|------|------|------|
| 트리거 | 파일 생성 감지 또는 수동 | 오픈클로 |
| 저장 | Google Drive / 공유 폴더 저장 | 오픈클로 |
| 알림 | Slack DM 또는 이메일 발송 | 오픈클로 (선택) |
| 실패 시 | 에러 로그 → Slack 알림 | 오픈클로 |

---

## 4. end-to-end 스모크 테스트 시나리오

```bash
# 1. 파이프라인 실행
python run.py --input data/sample/test_5.jsonl --out output/

# 2. Cowork 문서 생성 (수동)
# Cowork에서 "output/report_partial.json 읽고 보고서 작성" 요청

# 3. 오픈클로 트리거 확인
# output/cowork_doc_out_*.md 파일 생성 여부 확인

# 4. Drive 저장 확인
# Google Drive 공유 폴더에서 파일 확인
```

**테스트 결과:** 총 소요 시간 약 45초, 전체 시나리오 통과 ✅

---

## 5. 운영 RUNBOOK

1. `python run.py` 실행 → `output/report_partial.json` 생성 확인
2. Cowork에 보고서 작성 요청 → `cowork_doc_out_YYYYMMDD.md` 확인
3. 오픈클로 수동 트리거 실행 → Drive 저장 확인
4. 실패 시: `output/error.log` 확인 후 각 단계 개별 재실행

## 참고
- 진행 메모: `progress_w6.md`
- 데모 스크립트: `w6d4/md/demo_script_w6.md`
