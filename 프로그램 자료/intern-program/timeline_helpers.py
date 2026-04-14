# -*- coding: utf-8 -*-
"""Helpers for building HTML timeline blocks (①②③ style)."""


def item(t: str, title: str, lines: list[tuple[str, str]]) -> str:
    markers = "①②③④⑤⑥⑦⑧⑨⑩"
    parts = []
    for i, (k, v) in enumerate(lines):
        parts.append(f"{markers[i]} <strong>{k}</strong> — {v}")
    desc = "<br>".join(parts)
    return (
        f'<div class="tl-item"><div class="tl-time">{t}</div>'
        f'<div class="tl-title">{title}</div><div class="tl-desc">{desc}</div></div>'
    )


def wrap(*items: str) -> str:
    return '<div class="timeline">' + "".join(items) + "</div>"
