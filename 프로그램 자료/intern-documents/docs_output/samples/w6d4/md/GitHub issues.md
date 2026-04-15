# GitHub 이슈 목록 — W6D4

**날짜:** 2026-05-21 (목)
**일정:** W6D4 — 중간 점검 — 데모·피드백 반영
**작성자:** 인턴

---

## 오픈 이슈

| # | 제목 | 라벨 | 우선순위 | 상태 |
|---|------|------|---------|------|
| #1 | 수집 스크립트 재시도 로직 추가 | enhancement | Should | ✅ Closed |
| #2 | 전처리 PII 마스킹 패턴 확장 | enhancement | Should | ✅ Closed |
| #3 | 분류 정확도 85% 달성 | milestone | Must | 🔄 In Progress |
| #4 | README 카테고리 정의 섹션 추가 | documentation | Must | ✅ Closed (당일) |
| #5 | 신뢰도 0.7 미만 건 수동 검수 플로우 | enhancement | Should | ⬜ Todo |
| #6 | 분류 결과 시각화 (차트 1개) | feature | Should | ⬜ Todo |
| #7 | 실패 청크 자동 재처리 | enhancement | Could | ⬜ Todo |

---

## 이슈 #3 세부 내용

**목표:** 분류 정확도 82% → 83% 이상 달성

**시도 계획:**
1. 카테고리별 경계 케이스 예시 추가 (v0.3 프롬프트)
2. 신뢰도 0.75 미만 건 재시도 (다른 temperature로)
3. 골드셋 20건 → 30건으로 확대

**완료 기준:** 골드셋 30건 기준 정확도 ≥ 83%

---

## 이슈 #6 세부 내용

**목표:** 카테고리별 분포 막대 차트 1개 추가

**구현 계획:**
```python
# visualize.py
import matplotlib.pyplot as plt
import json

def plot_category_dist(report_path, out_path):
    with open(report_path) as f:
        data = json.load(f)
    cats = [d['category'] for d in data]
    # Counter → 막대 그래프
    ...
```

**완료 기준:** PNG 파일 생성 + README에 이미지 링크 추가

## 참고
- 멘토 중간 점검: `mid_review_w6.md`
- 커밋 메시지 규칙: `feat:` / `fix:` / `docs:` / `chore:`
