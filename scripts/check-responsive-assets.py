#!/usr/bin/env python3
"""Check the public screenshot set and reject audit-only captures."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCALES = ("zh-Hans", "en")
REQUIRED_SCREENSHOTS = (
    "01-mac-voice-follow.png",
    "01-iphone-remote-paragraph-3.png",
    "03-watch-remote-paragraph-3.png",
    "02-mac-script.png",
    "03-practice-library.png",
    "06-mac-prompter-recording.png",
    "07-mac-export-editor.png",
    "08-mac-transcript-comparison.png",
)


def main() -> int:
    errors: list[str] = []
    references: set[str] = set()
    for html_path in ROOT.rglob("*.html"):
        content = html_path.read_text(encoding="utf-8")
        for match in re.findall(r'(?:src|srcset|href|content)="([^"]+\.(?:png|webp))"', content):
            cleaned = match.replace("https://scriptpace.github.io/", "")
            if cleaned.startswith("../"):
                references.add(str((html_path.parent / cleaned).resolve().relative_to(ROOT)))
            elif cleaned.startswith("assets/"):
                references.add(cleaned)

    # Enforce 1:1 locale screenshot symmetry and WebP availability
    zh_files = {p.name for p in (ROOT / "assets/screenshots/zh-Hans").glob("*.png")}
    en_files = {p.name for p in (ROOT / "assets/screenshots/en").glob("*.png")}
    if zh_files != en_files:
        errors.append(f"screenshot locale mismatch: zh-Hans={sorted(zh_files - en_files)} en={sorted(en_files - zh_files)}")

    for locale in LOCALES:
        og_card = f"assets/og/{locale}/social-card.png"
        og_path = ROOT / og_card
        if not og_path.is_file() or og_path.stat().st_size == 0:
            errors.append(f"missing or empty OG card: {og_card}")
        elif og_card not in references:
            errors.append(f"OG card is not referenced by a page: {og_card}")

        for filename in REQUIRED_SCREENSHOTS:
            png_rel = f"assets/screenshots/{locale}/{filename}"
            webp_rel = png_rel.replace(".png", ".webp")
            for rel in (png_rel, webp_rel):
                path = ROOT / rel
                if not path.is_file() or path.stat().st_size == 0:
                    errors.append(f"missing or empty asset: {rel}")
                elif rel not in references:
                    errors.append(f"asset is not referenced by a page: {rel}")
            webp_path = ROOT / webp_rel
            if webp_path.is_file() and webp_path.stat().st_size > 350 * 1024:
                errors.append(f"WebP asset exceeds 350 KB budget: {webp_rel} ({webp_path.stat().st_size} bytes)")

    for brand_file in (ROOT / "assets/brand").glob("*"):
        if "artwork" in brand_file.name.lower():
            errors.append(f"forbidden concept artwork in assets/brand: {brand_file.name}")

    for forbidden in ("validation", "fixture"):
        if any(forbidden in str(path.relative_to(ROOT)) for path in ROOT.rglob("*") if path.is_file()):
            errors.append(f"audit-only directory is present in public site: {forbidden}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("all symmetric bilingual screenshots, WebP variants, and OG social cards are present and referenced")
    return 0


if __name__ == "__main__":
    sys.exit(main())
