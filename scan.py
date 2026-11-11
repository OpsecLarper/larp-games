#!/usr/bin/env python3
"""
scan.py — LARP Games index generator
Run this any time you add or remove games from the games/ folder.

Usage:
    python scan.py

It scans games/*.html and writes games/index.json so the site
can discover your games without a backend.
"""

import json
import os
import re
from pathlib import Path

GAMES_DIR = Path(__file__).parent / "games"


def file_to_name(filename: str) -> str:
    """Convert a filename like 'my-cool-game.html' → 'My Cool Game'."""
    name = re.sub(r"\.html?$", "", filename, flags=re.IGNORECASE)
    name = re.sub(r"[-_]+", " ", name)
    return name.title()


def scan():
    if not GAMES_DIR.exists():
        GAMES_DIR.mkdir()
        print(f"Created {GAMES_DIR}")

    html_files = sorted(
        f.name for f in GAMES_DIR.iterdir()
        if f.is_file() and f.suffix.lower() in {".html", ".htm"}
    )

    games = [
        {"name": file_to_name(f), "file": f}
        for f in html_files
    ]

    index_path = GAMES_DIR / "index.json"
    with open(index_path, "w", encoding="utf-8") as fh:
        json.dump(games, fh, indent=2, ensure_ascii=False)

    print(f"Found {len(games)} game(s):")
    for g in games:
        print(f"  • {g['name']}  ({g['file']})")
    print(f"\nWrote {index_path}")


if __name__ == "__main__":
    scan()
