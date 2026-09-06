#!/usr/bin/env python3
"""Check internal HTML links and local asset references."""

from __future__ import annotations

import html.parser
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]


class LinkParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "a" and values.get("href"):
            self.links.append(("href", values["href"] or ""))
        if tag == "img" and values.get("src"):
            self.links.append(("src", values["src"] or ""))


def resolve(source: Path, value: str) -> Path | None:
    parsed = urlparse(value)
    if parsed.scheme or parsed.netloc or value.startswith("#"):
        return None
    clean = parsed.path
    if not clean:
        return None
    if clean.startswith("/"):
        return ROOT / clean.lstrip("/")
    return (source.parent / clean).resolve()


def main() -> int:
    errors: list[str] = []
    for source in sorted(ROOT.rglob("*.html")):
        parser = LinkParser()
        parser.feed(source.read_text(encoding="utf-8"))
        for kind, value in parser.links:
            target = resolve(source, value)
            if target is None:
                continue
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{source.relative_to(ROOT)}: {kind} escapes site root: {value}")
                continue
            if target.is_dir():
                target = target / "index.html"
            if not target.is_file():
                errors.append(f"{source.relative_to(ROOT)}: missing {kind} target: {value}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("internal links and assets passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
