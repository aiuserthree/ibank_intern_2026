# 회귀 테스트 기록 — W7D1

**날짜:** 2026-05-25 (월)
**일정:** W7D1 — 기능 완성 & 엣지 케이스
**작성자:** 인턴

---

## 1. 테스트 스위트 구성

| 테스트 파일 | 대상 모듈 | 케이스 수 |
|-----------|---------|---------|
| test_collect.py | collect_raw.py | 8개 |
| test_preprocess.py | preprocess.py | 12개 |
| test_classify.py | classify.py | 6개 |
| test_pipeline_e2e.py | pipeline_core.py | 3개 |

---

## 2. 회귀 테스트 실행 결과

```bash
python -m pytest tests/ -v --tb=short
```

```
PASSED  test_collect.py::test_empty_input
PASSED  test_collect.py::test_encoding_euckr
PASSED  test_collect.py::test_large_doc_chunking
PASSED  test_preprocess.py::test_html_strip
PASSED  test_preprocess.py::test_pii_masking
PASSED  test_preprocess.py::test_chunk_200chars
PASSED  test_classify.py::test_batch_10
PASSED  test_classify.py::test_json_parse_error
PASSED  test_pipeline_e2e.py::test_5_docs
FAILED  test_collect.py::test_special_chars   ← E-04 미완성
FAILED  test_collect.py::test_duplicate_id    ← E-05 미완성

11 passed, 2 failed in 14.3s
```

---

## 3. 기존 버그 재발 확인

| 버그 | 최초 발생 | 재발 여부 |
|------|---------|---------|
| JSON 파싱 실패 시 크래시 | W6D2 | ✅ 재발 없음 |
| 빈 텍스트 NullPointerError | W6D1 | ✅ 재발 없음 |
| UTF-8 BOM 인코딩 오류 | W6D3 | ✅ 재발 없음 |

---

## 4. 수동 데모 시나리오 체크리스트

```
[ ✅ ] 1. data/sample/demo_input_10.jsonl 입력으로 run.py 실행
[ ✅ ] 2. output/demo_result.json 생성 확인
[ ✅ ] 3. 결과 JSON 스키마 일치 확인
[ ✅ ] 4. 분류 분포 요약 출력 확인
[ ✅ ] 5. 처리 시간 15초 이내 확인
[ ⬜ ] 6. 특수문자 포함 입력 처리 (E-04)
[ ⬜ ] 7. 중복 ID 처리 (E-05)
```

---

## 5. 내일 이전 수정 목록

1. E-04: 특수문자 정규화 개선 (`preprocess.py` line 45)
2. E-05: 중복 ID 필터 추가 (`collect_raw.py` line 89)
3. test_collect.py FAILED 2개 수정

## 참고
- 엣지 케이스 목록: `edge_cases_w7.md`
- 커밋: `fix: handle edge cases E-01~03, E-06~07`
