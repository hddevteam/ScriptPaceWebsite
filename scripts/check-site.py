#!/usr/bin/env python3
"""Validate localized ScriptPace pages and public content boundaries."""

from __future__ import annotations

import html.parser
import re
import sys
from pathlib import Path


SITE_ORIGIN = "https://scriptpace.github.io"
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
    "scriptpace-ultra-recording-artwork",
    "尚未发布",
    "尚未开放",
    "暂未开放",
    "not yet available",
    "not available yet",
)
FORBIDDEN_ALL_PAGE_PATTERNS = (
    "尚未发布",
    "尚未开放",
    "尚未在当前版本开放",
    "尚未在 app store 上架",
    "暂未开放",
    "not yet available",
    "not available yet",
    "not listed on the app store yet",
    "not available in the current release",
    "把当前可用权益",
    "把练习语音与录制素材的边界说清楚",
    "把产品边界说清楚",
    "我们不会做什么",
    "see today's prompting access",
    "现在即可将",
)
PRODUCTION_DRAFT_PATTERNS = (
    "product draft",
    "隐私政策草案",
    "support email will be configured before public release",
    "支持邮箱会在正式发布前配置",
    "cannot be used as the final privacy policy URL",
    "不能作为最终隐私政策 URL",
)


class PageParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: list[str] = []
        self.attributes: dict[str, list[dict[str, str]]] = {}
        self.text: list[str] = []
        self.jsonld_blocks: list[str] = []
        self._in_jsonld = False
        self._jsonld_buf: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {key.lower(): value or "" for key, value in attrs}
        self.tags.append(tag)
        self.attributes.setdefault(tag, []).append(attr_map)
        if tag == "script" and attr_map.get("type", "").lower() == "application/ld+json":
            self._in_jsonld = True
            self._jsonld_buf = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._in_jsonld:
            self.jsonld_blocks.append("".join(self._jsonld_buf).strip())
            self._in_jsonld = False

    def handle_data(self, data: str) -> None:
        if self._in_jsonld:
            self._jsonld_buf.append(data)
        else:
            self.text.append(data)

    @property
    def content(self) -> str:
        return " ".join(self.text).lower()


def fail(message: str) -> None:
    print(f"ERROR: {message}")


def expected_canonical(relative: Path) -> str:
    rel_str = relative.as_posix()
    if rel_str == "index.html":
        return f"{SITE_ORIGIN}/"
    if rel_str.endswith("/index.html"):
        prefix = rel_str[: -len("index.html")]
        return f"{SITE_ORIGIN}/{prefix}"
    return f"{SITE_ORIGIN}/{rel_str}"


def validate_seo_and_images(path: Path, parser: PageParser, errors: list[str]) -> None:
    import json

    relative = path.relative_to(ROOT)
    expected_url = expected_canonical(relative)

    links = parser.attributes.get("link", [])
    canonicals = [l.get("href", "") for l in links if l.get("rel") == "canonical"]
    if canonicals != [expected_url]:
        errors.append(f"{relative}: expected canonical {expected_url}, got {canonicals}")

    hreflangs = {
        l.get("hreflang", ""): l.get("href", "")
        for l in links
        if l.get("rel") == "alternate" and l.get("hreflang")
    }
    for required_lang in ("zh-Hans", "en", "x-default"):
        if not hreflangs.get(required_lang, "").startswith(f"{SITE_ORIGIN}/"):
            errors.append(f"{relative}: missing or invalid hreflang={required_lang}")

    metas: dict[str, str] = {}
    for meta in parser.attributes.get("meta", []):
        key = meta.get("name") or meta.get("property")
        if key:
            metas[key.lower()] = meta.get("content", "")

    for required_meta in ("description", "og:title", "og:description", "og:type", "og:url", "og:image", "og:locale", "twitter:card"):
        if not metas.get(required_meta):
            errors.append(f"{relative}: missing meta {required_meta}")
    if metas.get("og:url") and metas["og:url"] != expected_url:
        errors.append(f"{relative}: og:url {metas['og:url']} does not match canonical {expected_url}")

    for img in parser.attributes.get("img", []):
        src = img.get("src", "<unknown>")
        width = img.get("width", "")
        height = img.get("height", "")
        if not (width.isdigit() and int(width) > 0 and height.isdigit() and int(height) > 0):
            errors.append(f"{relative}: img {src} missing explicit positive width/height")

    if relative.as_posix() in ("zh-hans/index.html", "en/index.html"):
        section_ids = {attrs.get("id", "") for attrs in parser.attributes.get("section", [])}
        for required_section in ("teleprompter", "pro", "scenarios", "recording", "plans"):
            if required_section not in section_ids:
                errors.append(f"{relative}: missing required homepage section #{required_section}")
        if not parser.jsonld_blocks:
            errors.append(f"{relative}: missing SoftwareApplication JSON-LD")
        for raw in parser.jsonld_blocks:
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"{relative}: invalid JSON-LD: {exc}")
                continue
            if payload.get("@type") != "SoftwareApplication":
                errors.append(f"{relative}: expected SoftwareApplication JSON-LD")
            raw_offers = json.dumps(payload.get("offers", []))
            if "29.99" in raw_offers or "89.99" in raw_offers:
                errors.append(f"{relative}: JSON-LD offers must not list unpublished Ultra pricing")

    if relative.as_posix() in ("zh-hans/support.html", "en/support.html"):
        if not parser.jsonld_blocks:
            errors.append(f"{relative}: missing FAQPage JSON-LD")
        for raw in parser.jsonld_blocks:
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"{relative}: invalid JSON-LD: {exc}")
                continue
            if payload.get("@type") != "FAQPage" or len(payload.get("mainEntity", [])) < 5:
                errors.append(f"{relative}: expected FAQPage JSON-LD with at least 5 questions")


def validate_page(path: Path, errors: list[str], *, localized: bool = True) -> None:
    raw_html = path.read_text(encoding="utf-8")
    parser = PageParser()
    parser.feed(raw_html)
    relative = path.relative_to(ROOT)
    if 'lang="' not in raw_html:
        errors.append(f"{relative}: missing html language attribute")
    if '<meta name="viewport"' not in raw_html:
        errors.append(f"{relative}: missing viewport meta")
    if not any(attrs.get("class") == "skip-link" for attrs in parser.attributes.get("a", [])):
        errors.append(f"{relative}: missing skip link")
    if len(parser.attributes.get("h1", [])) != 1:
        errors.append(f"{relative}: expected exactly one h1")
    validate_seo_and_images(path, parser, errors)
    for forbidden in FORBIDDEN_ALL_PAGE_PATTERNS:
        if forbidden.lower() in parser.content or forbidden.lower() in raw_html.lower():
            errors.append(f"{relative}: forbidden negative release status phrasing: {forbidden}")
    if localized:
        required_paths = ("privacy.html", "terms.html", "support.html")
        for required in required_paths:
            if f'href="{required}"' not in raw_html:
                errors.append(f"{relative}: missing local {required} link")
        if 'data-language-switch="' not in raw_html:
            errors.append(f"{relative}: missing language switch")
        if path.name in MARKETING_PAGES:
            for forbidden in FORBIDDEN_MARKETING_PATTERNS:
                if forbidden.lower() in parser.content or forbidden.lower() in raw_html.lower():
                    errors.append(f"{relative}: forbidden marketing claim or asset: {forbidden}")
            if relative.parts[0] == "zh-hans" and "hear it. practice it." in parser.content:
                errors.append(f"{relative}: unlocalized English placeholder text on Chinese page")


def validate_crawl_files(errors: list[str]) -> None:
    import xml.etree.ElementTree as ET

    robots = ROOT / "robots.txt"
    if not robots.is_file():
        errors.append("missing robots.txt")
    elif f"Sitemap: {SITE_ORIGIN}/sitemap.xml" not in robots.read_text(encoding="utf-8"):
        errors.append("robots.txt: missing canonical Sitemap declaration")

    sitemap = ROOT / "sitemap.xml"
    if not sitemap.is_file():
        errors.append("missing sitemap.xml")
    else:
        try:
            tree = ET.parse(sitemap)
            locs = [el.text.strip() for el in tree.getroot().iter() if el.tag.endswith("loc") and el.text]
            if len(locs) < 11:
                errors.append(f"sitemap.xml: expected at least 11 URLs, got {len(locs)}")
        except ET.ParseError as exc:
            errors.append(f"sitemap.xml: XML parse error: {exc}")


def main() -> int:
    production = "--production" in sys.argv[1:]
    errors: list[str] = []
    root_index = ROOT / "index.html"
    if not root_index.is_file():
        errors.append("missing index.html")
    else:
        validate_page(root_index, errors, localized=False)
    for locale in LOCALES:
        for page in PAGES:
            path = ROOT / locale / page
            if not path.is_file():
                errors.append(f"missing page: {path.relative_to(ROOT)}")
                continue
            validate_page(path, errors)
            if production:
                content = path.read_text(encoding="utf-8").lower()
                for forbidden in PRODUCTION_DRAFT_PATTERNS:
                    if forbidden.lower() in content:
                        errors.append(
                            f"{path.relative_to(ROOT)}: draft or preview release text remains: {forbidden}"
                        )
    validate_crawl_files(errors)
    config = ROOT / "site-config.js"
    if not config.is_file():
        errors.append("missing site-config.js")
    else:
        config_text = config.read_text(encoding="utf-8")
        if f'siteOrigin: "{SITE_ORIGIN}"' not in config_text:
            errors.append("site-config.js: missing canonical siteOrigin")
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
