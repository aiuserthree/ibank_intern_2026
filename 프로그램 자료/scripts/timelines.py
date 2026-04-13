"""40일 전체 타임라인 — generate_pages.py에서 import."""
from timelines_w1 import TIMELINES as TW1
from timelines_w2 import TIMELINES as TW2
from timelines_w3 import TIMELINES as TW3
from timelines_w4 import TIMELINES as TW4
from timelines_w5 import TIMELINES as TW5
from timelines_w6 import TIMELINES as TW6
from timelines_w7 import TIMELINES as TW7
from timelines_w8 import TIMELINES as TW8

TIMELINES: dict = {}
for T in (TW1, TW2, TW3, TW4, TW5, TW6, TW7, TW8):
    TIMELINES.update(T)

if len(TIMELINES) != 40:
    raise RuntimeError(f"TIMELINES must have 40 keys, got {len(TIMELINES)}")
