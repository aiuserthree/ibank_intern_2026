# 라이선스 및 출처 — W7D2

**날짜:** 2026-05-26 (화)
**일정:** W7D2 — 산출물 패키징 — README·폴더·라이선스
**작성자:** 인턴

---

## 1. 프로젝트 라이선스

**라이선스 유형:** MIT License

```
MIT License

Copyright (c) 2026 인턴 (Junhyung Cho)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 2. 외부 라이브러리 출처

| 라이브러리 | 버전 | 라이선스 | 용도 |
|-----------|------|---------|------|
| openai | 1.30.0 | MIT | LLM API 호출 |
| requests | 2.32.0 | Apache 2.0 | HTTP 요청 |
| pandas | 2.2.0 | BSD 3-Clause | 데이터 처리 |
| matplotlib | 3.8.0 | PSF | 시각화 |
| pytest | 8.2.0 | MIT | 테스트 |
| python-dotenv | 1.0.1 | BSD | 환경변수 관리 |

---

## 3. 데이터 출처 및 저작권

| 데이터 | 출처 | 라이선스 | 수집 방법 |
|--------|------|---------|---------|
| 공공기관 AI 보도자료 | 각 기관 공식 홈페이지 | 공공누리 제1유형 | RSS / 웹 스크래핑 |
| 정부 정책 발표문 | 행정안전부 | 공공누리 제1유형 | 공개 API |
| 뉴스 기사 요약 | 공개 뉴스 RSS | 보도 목적 인용 한도 내 | RSS 피드 |

**주의:**
- 원본 데이터는 재배포 불가 (공공누리 제1유형 조건)
- `data/sample/` 폴더에는 비식별화·축소된 샘플만 포함
- PII(개인정보) 제거 완료 확인

---

## 4. 재배포 금지 항목

- 원본 수집 데이터 (data/raw/) — 저장소에 포함하지 않음
- API 키 및 인증 정보 (.env) — .gitignore로 제외
- 멘토 피드백 원문 — 내부 공유 목적으로만 사용

## 참고
- 패키징 노트: `docs/package_notes_w7.md`
- 샘플 데이터 설명: `data/sample/README.md`
