#!/usr/bin/env python3
"""
Non-writing readiness checks for the Nurovelle homepage.

The script validates local HTML links/assets, branch dropdown consistency and
live GET endpoints. It intentionally does not submit forms or create leads.
"""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
HOMEPAGE_DIR = ROOT / "homepage"

EXPECTED_BRANCHES = [
    "Energie & Versorgung",
    "Finanzen & Versicherung",
    "Industrie & Produktion",
    "Verwaltung, Vertrieb, Einkauf & Marketing",
    "Gesundheitswesen & Pflege",
    "Immobilien & Facility Management",
    "Bildung & Forschung",
    "Dienstleistungen & KMU",
    "Sonstiges",
]

LIVE_GET_URLS = [
    "https://nurovelle.de/",
    "https://nurovelle.de/homepage/index.html",
    "https://nurovelle.de/homepage/analyse.html",
    "https://nurovelle.de/homepage/impressum.html",
    "https://nurovelle.de/homepage/datenschutz.html",
    "https://nurovelle.de/api/v1/questions?industry=service&tier=basic&include_risk=false",
    "https://nurovelle.de/api/v1/questions?industry=manufacturing&tier=basic&include_risk=false",
    "https://nurovelle.de/api/v1/questions?industry=care&tier=basic&include_risk=false",
]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.hrefs: list[str] = []
        self.assets: list[str] = []
        self.branch_options: list[str] = []
        self._in_branch_select = False
        self._in_option = False
        self._option_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key: value or "" for key, value in attrs}
        if data.get("id"):
            self.ids.add(data["id"])
        if tag == "select" and data.get("name") == "branche":
            self._in_branch_select = True
        elif self._in_branch_select and tag == "option":
            self._in_option = True
            self._option_text = []

        href = data.get("href")
        if href:
            self.hrefs.append(href.strip())
        src = data.get("src")
        if src:
            self.assets.append(src.strip())

    def handle_data(self, data: str) -> None:
        if self._in_option:
            self._option_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self._in_branch_select and tag == "option":
            option = " ".join("".join(self._option_text).split())
            if option and not option.endswith("auswaehlen") and not option.endswith("auswählen"):
                self.branch_options.append(option)
            self._in_option = False
            self._option_text = []
        elif self._in_branch_select and tag == "select":
            self._in_branch_select = False


def parse_page(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    return parser


def is_external(value: str) -> bool:
    return value.startswith(("http://", "https://", "mailto:", "tel:", "#"))


def local_html_pages() -> list[Path]:
    return [HOMEPAGE_DIR / "index.html", HOMEPAGE_DIR / "analyse.html"]


def check_local_links() -> list[str]:
    errors: list[str] = []
    for page in local_html_pages():
        parsed = parse_page(page)
        for href in parsed.hrefs:
            if is_external(href):
                continue
            target, _, anchor = href.partition("#")
            target_file = (page.parent / target).resolve() if target else page.resolve()
            if target and not target_file.exists():
                errors.append(f"{page.relative_to(ROOT)} missing href target: {href}")
                continue
            if anchor and target_file.suffix.lower() == ".html":
                target_parser = parse_page(target_file)
                if anchor not in target_parser.ids:
                    errors.append(f"{page.relative_to(ROOT)} missing anchor: {href}")
        for asset in parsed.assets:
            if is_external(asset):
                continue
            asset_target = asset.split("#", 1)[0].split("?", 1)[0]
            if asset_target and not (page.parent / asset_target).resolve().exists():
                errors.append(f"{page.relative_to(ROOT)} missing asset: {asset}")
    return errors


def check_branches() -> list[str]:
    errors: list[str] = []
    for page in local_html_pages():
        branches = parse_page(page).branch_options
        if branches != EXPECTED_BRANCHES:
            errors.append(f"{page.relative_to(ROOT)} branch mismatch: {branches}")
    return errors


def check_live_gets(urls: Iterable[str]) -> list[str]:
    errors: list[str] = []
    for url in urls:
        request = urllib.request.Request(url, method="GET", headers={"User-Agent": "nurovelle-readiness-check/1.0"})
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                status = response.getcode()
                if status < 200 or status >= 400:
                    errors.append(f"{url} returned HTTP {status}")
        except urllib.error.HTTPError as error:
            errors.append(f"{url} returned HTTP {error.code}")
        except Exception as error:
            errors.append(f"{url} failed: {error}")
    return errors


def main() -> int:
    checks = {
        "local_links_assets": check_local_links(),
        "branch_dropdowns": check_branches(),
        "live_get_endpoints": check_live_gets(LIVE_GET_URLS),
    }
    passed = all(not errors for errors in checks.values())
    print(json.dumps({"passed": passed, "checks": checks}, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
