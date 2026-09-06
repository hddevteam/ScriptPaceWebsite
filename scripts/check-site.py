#!/usr/bin/env python3
"""Validate localized ScriptPace pages and public content boundaries."""

from __future__ import annotations

import html.parser
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCALES = ("zh-hans", "en")
PAGES = ("index.html", "features.html", "support.html", "privacy.html", "terms.html")
MARKETING_PAGES = {"index.html", "features.html"}
FORBIDDEN_MARKETING_PATTERNS = (
    "自动改稿",
    "云端写作",
    "cloud writing",
    "perfect recognition",
    "record and save raw microphone audio",
    "会保存原始麦克风音频",
    "separate watch purchase",
)


class PageParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: list[str] = []
        self.attributes: dict[str, list[dict[str, str]]] = {}
        self.text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.append(tag)
        self.attributes.setdefault(tag, []).append({key: value or "" for key, value in attrs})

    def handle_data(self, data: str) -> None:
        self.text.append(data)

    @property
    def content(self) -> str:
        return " ".join(self.text).lower()


def fail(message: str) -> None:
    print(f"ERROR: {message}")


def validate_page(path: Path, errors: list[str]) -> None:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    relative = path.relative_to(ROOT)
    if "lang=\"" not in path.read_text(encoding="utf-8"):
        errors.append(f"{relative}: missing html language attribute")
    if '<meta name="viewport"' not in path.read_text(encoding="utf-8"):
        errors.append(f"{relative}: missing viewport meta")
    if not any(attrs.get("class") == "skip-link" for attrs in parser.attributes.get("a", [])):
        errors.append(f"{relative}: missing skip link")
    if len(parser.attributes.get("h1", [])) != 1:
        errors.append(f"{relative}: expected exactly one h1")
    required_paths = ("privacy.html", "terms.html", "support.html")
    for required in required_paths:
        if f'href="{required}"' not in path.read_text(encoding="utf-8"):
            errors.append(f"{relative}: missing local {required} link")
    if 'data-language-switch="' not in path.read_text(encoding="utf-8"):
        errors.append(f"{relative}: missing language switch")
    if path.name in MARKETING_PAGES:
        for forbidden in FORBIDDEN_MARKETING_PATTERNS:
            if forbidden.lower() in parser.content:
                errors.append(f"{relative}: forbidden marketing claim: {forbidden}")


def main() -> int:
    production = "--production" in sys.argv[1:]
    errors: list[str] = []
    for locale in LOCALES:
        for page in PAGES:
            path = ROOT / locale / page
            if not path.is_file():
                errors.append(f"missing page: {path.relative_to(ROOT)}")
                continue
            validate_page(path, errors)
    config = ROOT / "site-config.js"
    if not config.is_file():
        errors.append("missing site-config.js")
    else:
        config_text = config.read_text(encoding="utf-8")
        if 'appStoreURL: "https://' not in config_text:
            errors.append("site-config.js: missing App Store URL")
        if 'supportEmail: ""' not in config_text:
            print("INFO: support email configured")
        else:
            if production:
                errors.append("site-config.js: supportEmail is required for production deployment")
            else:
                print("INFO: support email is not configured; production deployment remains blocked")
    for error in errors:
        fail(error)
    if errors:
        return 1
    print("site structure and content checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
