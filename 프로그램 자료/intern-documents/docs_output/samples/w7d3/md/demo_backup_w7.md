# 데모 백업 자료 — W7D3

**날짜:** 2026-05-27 (수)
**일정:** W7D3 — PPT 완성 & 데모 스크립트 동결
**작성자:** 인턴
**용도:** 네트워크 장애·실행 오류 시 백업

---

## 백업 시나리오

### 시나리오 A: API 연결 실패
→ 사전 캡처된 실행 결과 스크린샷 PPT 부록으로 전환

### 시나리오 B: 코드 실행 오류
→ output/expected_demo.json 직접 열어 결과 설명

### 시나리오 C: 노트북 장애
→ USB에 presentation_final_w7.pdf + expected_demo.json 저장

---

## 사전 캡처 스크린샷 목록

| 번호 | 파일명 | 캡처 내용 |
|------|-------|---------|
| 1 | demo_run_success.png | run.py 실행 성공 터미널 |
| 2 | demo_result_json.png | output/demo_result.json 내용 |
| 3 | demo_distribution.png | 카테고리 분포 출력 |

---

## 사전 준비 결과 JSON (expected_demo.json 요약)

```
doc_d01: 민원·행정 자동화 (0.94)
doc_d02: 의료·복지 AI (0.88)
doc_d03: 데이터 분석·예측 (0.91)
doc_d04: 챗봇·대화형 서비스 (0.85)
doc_d05: 민원·행정 자동화 (0.92)
doc_d06: 교육·연구 AI (0.79)
doc_d07: 데이터 분석·예측 (0.90)
doc_d08: 의료·복지 AI (0.83)
doc_d09: 민원·행정 자동화 (0.87)
doc_d10: 챗봇·대화형 서비스 (0.81)
```

**분포:** 민원·행정 자동화 3건 / 의료·복지 AI 2건 / 데이터 분석·예측 2건 / 챗봇·대화형 서비스 2건 / 교육·연구 AI 1건

---

## USB 저장 체크리스트

- [x] presentation_final_w7.pdf
- [x] presentation_final_w7.pptx
- [x] output/expected_demo.json
- [x] docs/demo_run_success.png
- [x] docs/demo_result_json.png

## 참고
- 최종 데모 스크립트: `demo_script_final.md`
