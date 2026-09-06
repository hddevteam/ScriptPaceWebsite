#!/usr/bin/env python3
"""Check the public screenshot set and reject audit-only captures."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = tuple(
    f"assets/screenshots/{locale}/{filename}"
    for locale, filename in (
        ("zh-Hans", "01-mac-voice-follow.png"),
        ("zh-Hans", "01-iphone-remote-paragraph-3.png"),
        ("zh-Hans", "03-watch-remote-paragraph-3.png"),
        ("en", "01-mac-voice-follow.png"),
        ("en", "01-iphone-remote-paragraph-3.png"),
        ("en", "03-watch-remote-paragraph-3.png"),
    )
)


def main() -> int:
    errors: list[str] = []
    references: set[str] = set()
    for html_path in ROOT.rglob("*.html"):
        content = html_path.read_text(encoding="utf-8")
        for match in re.findall(r"(?:src|href)=\"([^\"]+\.png)\"", content):
            if match.startswith("../"):
                references.add(str((html_path.parent / match).resolve().relative_to(ROOT)))
            elif match.startswith("assets/"):
                references.add(match)
    for relative in EXPECTED:
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing or empty screenshot: {relative}")
        if relative not in references:
            errors.append(f"screenshot is not referenced by a page: {relative}")
    for forbidden in ("validation", "fixture"):
        if any(forbidden in str(path.relative_to(ROOT)) for path in ROOT.rglob("*") if path.is_file()):
            errors.append(f"audit-only directory is present in public site: {forbidden}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("all six synchronized public screenshots are present and referenced")
    return 0


if __name__ == "__main__":
    sys.exit(main())
