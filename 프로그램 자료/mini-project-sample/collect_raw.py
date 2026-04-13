#!/usr/bin/env python3
"""공개 샘플 CSV(VOC 리뷰)를 data/raw.csv로 복사·검증합니다. (교육용)"""
from __future__ import annotations

import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "data" / "sample_voc_reviews.csv"
DST = ROOT / "data" / "raw.csv"
REQUIRED = ("id", "date", "source_type", "app_name", "rating", "review_text")


def main() -> None:
    if not SRC.is_file():
        raise SystemExit(f"원본 없음: {SRC}")
    with SRC.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise SystemExit("CSV 헤더 없음")
        missing = set(REQUIRED) - set(reader.fieldnames)
        if missing:
            raise SystemExit(f"필수 컬럼 누락: {missing}")
    shutil.copyfile(SRC, DST)
    print(f"[collect_raw] 복사 완료: {DST}")


if __name__ == "__main__":
    main()
