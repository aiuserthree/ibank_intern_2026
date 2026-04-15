# 데이터 분석 노트 — W3D2

**날짜:** 2026-04-28 (화)  
**일정:** W3D2 — 데이터 분석 작성 & GA4 등 경험 자동화  
**작성자:** 인턴  
**상태:** 작성 완료

---

## 1. 분석 질문 정의

**비즈니스 질문:**  
> "지난 4주간 신규 방문자 중 어떤 채널에서 유입된 사용자가 가장 높은 전환율을 보이는가?"

### 핵심 지표 (3개)
| 지표 | 정의 | 측정 방법 |
|------|------|-----------|
| 전환율 | 목표 완료 / 세션 수 | GA4 Explore |
| 평균 체류시간 | 세션 내 총 참여 시간 평균 | `user_engagement_duration` |
| 이탈률 | 단일 페이지 세션 비율 | `bounced_sessions / sessions` |

### 세그먼트 축
- **채널**: Organic Search / Paid Search / Direct / Social
- **디바이스**: Desktop / Mobile

### 한계 사항
- GA4 샘플링: 세션 수 > 10만 이상이면 결과 왜곡 가능
- 쿠키 동의 미완료 사용자는 집계에서 제외됨

---

## 2. 데이터 확보 방법

### GA4 내보내기 경로
1. GA4 → 탐색(Explore) → 자유형식 보고서
2. 기간: 최근 28일, 일별 집계
3. CSV 내보내기 → `data/sample/ga_sample.csv`

### 데이터 정제 체크리스트
- [x] 날짜 형식 통일: `YYYY-MM-DD`
- [x] 타임존: Asia/Seoul UTC+9
- [x] PII 컬럼 제거: `user_id` → SHA-256 해시 처리
- [x] 이상치 표시: 세션 수 0 이하 행 플래그

---

## 3. pandas 분석 스크립트 요약

### 코드 패턴
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/sample/ga_sample.csv')
print(df.info())
print(df.describe())

# 채널별 전환율 집계
channel_summary = (
    df.groupby('channel')
    .agg(sessions=('sessions','sum'), conversions=('conversions','sum'))
    .assign(cvr=lambda x: x['conversions']/x['sessions']*100)
    .sort_values('cvr', ascending=False)
)
print(channel_summary)
```

### 분석 결과 (샘플)
| 채널 | 세션 | 전환 | 전환율 |
|------|------|------|--------|
| Organic Search | 8,420 | 382 | 4.5% |
| Paid Search | 3,105 | 186 | 6.0% |
| Direct | 2,890 | 98 | 3.4% |
| Social | 1,640 | 29 | 1.8% |

**인사이트:** Paid Search의 전환율이 가장 높지만 세션 볼륨이 작아 전체 기여도는 Organic이 더 높음.  
**반대 가능성:** Paid 캠페인 목적 페이지가 좁아 자연스럽게 높아 보일 수 있음.

---

## 4. 자동화 아이디어

### 후보 1: 주간 채널 리포트 자동 생성
- **트리거**: 매주 월요일 09:00
- **액션**: CSV 내보내기 → pandas 집계 → 메일 발송
- **위험**: 숫자 오류 시 잘못된 리포트 발송 → 알림 임계값 설정 필요

### 후보 2: 이상 세션 경보
- **트리거**: 일별 세션 수 전주 대비 -30% 이하
- **액션**: Slack 알림 발송
- **위험**: 공휴일 오탐 → 공휴일 캘린더 예외 처리 필요

---

## 5. 다음 단계

- `analytics_questions_w3.md` → 이 파일 기반으로 W3D3 API 파이프라인과 연계
- API 키 환경 설정 준비 (`.env.example` 작성)
- 4주차 자동화 실험 슬롯 캘린더에 표시

## 참고
- 출력 파일: `output/channel_summary.csv`, `output/channel_cvr_chart.png`
- 분석 스크립트: `src/analysis_w3d2.py`
