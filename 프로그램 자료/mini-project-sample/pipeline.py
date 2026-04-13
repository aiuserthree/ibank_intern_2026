#!/usr/bin/env python3
"""
서비스 리뷰·VOC AI 분석 대시보드 (샘플): raw.csv → report.json + output/md/insights_weekly.md

실제 과제는 LLM·Claude API로 감성·토픽 분류 후 Looker Studio / Next.js 대시보드·백엔드 연동.
여기서는 키워드 규칙으로 라벨을 생성해 재현·제출 형식을 맞춤.
"""
from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw.csv"
OUT_JSON = ROOT / "output" / "report.json"
OUT_MD = ROOT / "output" / "md" / "insights_weekly.md"
LOG = ROOT / "output" / "pipeline_run.log"

# VOC 토픽 (첫 매칭 우선 — 구체적 규칙을 위에)
VOC_TOPIC_RULES: list[tuple[str, tuple[str, ...]]] = [
    ("버그·오류", ("버그", "오류", "크래시", "튕김", "팝업", "안 열림", "안됨")),
    ("성능·속도", ("느림", "로딩", "속도", "렉", "멈춤", "개선 안")),
    ("가격·결제", ("가격", "결제", "구독", "환불", "프리미엄", "부담")),
    ("고객지원", ("문의", "답변", "고객센터", "채팅")),
    ("UX·UI", ("UI", "화면", "메뉴", "직관", "알림", "설정", "불편", "경로")),
    ("기능·콘텐츠", ("기능", "검색", "업데이트", "콘텐츠")),
]


def classify_voc_topic(text: str) -> str:
    for topic, kws in VOC_TOPIC_RULES:
        if any(k in text for k in kws):
            return topic
    return "기타"


def classify_sentiment_voc(text: str) -> str:
    neg = ("느림", "느려", "안됨", "오류", "불편", "부담", "버그", "팝업", "안 열림", "안됩니다", "부탁")
    pos = ("좋아", "좋았", "편해", "만족", "깔끔", "빠르", "빨라", "괜찮")
    if any(k in text for k in neg):
        return "부정"
    if any(k in text for k in pos):
        return "긍정"
    return "중립"


def evidence_line(review: str, topic: str, sentiment: str) -> str:
    return f"규칙 기반 분류: VOC토픽={topic}, 감성={sentiment}. (샘플: 키워드 매칭)"


def main() -> None:
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    if not RAW.is_file():
        raise SystemExit("data/raw.csv 없음. 먼저: python collect_raw.py")

    items = []
    with RAW.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            hid = int(row["id"])
            review = row["review_text"].strip()
            topic = classify_voc_topic(review)
            sentiment = classify_sentiment_voc(review)
            items.append(
                {
                    "id": hid,
                    "date": row["date"].strip(),
                    "source_type": row["source_type"].strip(),
                    "app_name": row["app_name"].strip(),
                    "rating": int(row["rating"]),
                    "review_excerpt": review[:80] + ("…" if len(review) > 80 else ""),
                    "voc_topic": topic,
                    "sentiment": sentiment,
                    "confidence": round(0.62 + (hid % 7) * 0.04, 2),
                    "evidence_one_liner": evidence_line(review, topic, sentiment),
                }
            )

    kst = timezone(timedelta(hours=9))
    now = datetime.now(kst).isoformat()
    voc_topics = ["버그·오류", "성능·속도", "가격·결제", "고객지원", "UX·UI", "기능·콘텐츠", "기타"]
    sentiments = ["긍정", "부정", "중립"]

    report = {
        "meta": {
            "project": "voc_ai_dashboard_sample",
            "project_title": "서비스 리뷰·VOC AI 분석 대시보드",
            "schema_version": "1.1",
            "generated_at": now,
            "model_note": "샘플: 키워드 규칙(실제 과제에서는 LLM 모델명·프롬프트 해시·Looker 연동 정보 기록)",
            "disclaimer": "교육용 가공 리뷰·평점은 샘플이며 실제 스토어와 무관합니다.",
        },
        "labels_definition": {
            "voc_topic": voc_topics,
            "sentiment": sentiments,
        },
        "items": items,
    }

    OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    topics_cnt = Counter(i["voc_topic"] for i in items)
    sent_cnt = Counter(i["sentiment"] for i in items)
    lines = [
        "# 주간 VOC 인사이트 브리핑 (파이프라인 생성)",
        "",
        "- **프로젝트:** 서비스 리뷰·VOC AI 분석 대시보드 (샘플)",
        f"- 생성 시각(KST): {now}",
        "- **주의:** 본 샘플은 API 없이 키워드 규칙으로 라벨을 붙였습니다. 실제 과제에서는 LLM 결과를 검증하세요.",
        "",
        "## VOC 토픽 분포",
        "",
        "| VOC 토픽 | 건수 |",
        "|------|------|",
    ]
    for k, v in sorted(topics_cnt.items()):
        lines.append(f"| {k} | {v} |")
    lines.extend(
        [
            "",
            "## 감성 분포",
            "",
            "| 감성 | 건수 |",
            "|------|------|",
        ]
    )
    for k in sentiments:
        lines.append(f"| {k} | {sent_cnt.get(k, 0)} |")
    lines.extend(
        [
            "",
            "## 시사점 (자동 초안)",
            "",
            "1. 부정 리뷰가 **성능·속도·버그**에 집중되면 해당 축을 우선 개선·모니터링 대상으로 삼습니다.",
            "2. 규칙 기반이므로 **아이러니·복합 문장**에 약합니다. LLM + 소량 검수로 전환하세요.",
            "3. `report.json`의 `confidence`는 샘플용 가중치입니다.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    log_line = f"{now}\tOK\trows={len(items)}\twritten={OUT_JSON.name},{OUT_MD.name}\n"
    with LOG.open("a", encoding="utf-8") as lf:
        lf.write(log_line)

    print(f"[pipeline] 완료: {OUT_JSON}, {OUT_MD}, 로그 추가: {LOG}")


if __name__ == "__main__":
    main()
