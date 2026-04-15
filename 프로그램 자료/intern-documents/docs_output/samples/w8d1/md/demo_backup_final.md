# 최종 데모 백업 자료 — W8D1

**날짜:** 2026-06-01 (월)
**일정:** W8D1 — 최종 발표 리허설 & 수치·슬라이드 동결
**작성자:** 인턴

---

## 백업 시나리오별 전환 방법

### 시나리오 A: API 연결 실패
1. 터미널 닫기
2. PPT 슬라이드 4로 이동 (데모 스크린샷)
3. 발표: "미리 캡처한 실행 결과로 설명하겠습니다."

### 시나리오 B: 코드 오류 발생
1. 터미널 닫기
2. `output/expected_demo.json` 파일 열기 (VS Code)
3. 결과 3건 직접 보여주며 설명

### 시나리오 C: 노트북 전원 오류
1. 발표 담당자에게 USB 전달
2. 다른 노트북에서 PDF로 진행

---

## USB 저장 확인 (최종)

| 파일 | 저장 여부 | 용량 |
|------|---------|------|
| presentation_final_w8_v3.pdf | 완료 | 2.1MB |
| presentation_final_w8_v3.pptx | 완료 | 4.3MB |
| output/expected_demo.json | 완료 | 8KB |
| docs/demo_run_success.png | 완료 | 145KB |
| docs/demo_result_json.png | 완료 | 132KB |
| docs/demo_distribution.png | 완료 | 98KB |

---

## 플랜 B 전환 신호

| 상황 | 신호 | 즉시 행동 |
|------|------|---------|
| 터미널 응답 없음 (5초) | API 실패 의심 | 시나리오 A 실행 |
| 에러 메시지 출력 | 코드 오류 | 시나리오 B 실행 |
| 화면 연결 끊김 | 장비 오류 | USB 전달 |

## 참고
- 동결 메모: `presentation_final_w8.md`
- 성과 수치: `performance_metrics_w8.md`
