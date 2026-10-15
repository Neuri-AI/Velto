"""Validate Mintlify navigation and internal documentation routes without Node."""
from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parents[2]
PUBLIC = WORKSPACE / "public"


class DocumentationLinkTests(unittest.TestCase):
    def test_navigation_pages_exist(self) -> None:
        navigation = json.loads((PUBLIC / "docs.json").read_text(encoding="utf-8"))["navigation"]
        missing: list[str] = []
        for group in navigation["groups"]:
            for route in group["pages"]:
                if not (PUBLIC / f"{route}.mdx").is_file():
                    missing.append(route)
        self.assertEqual(missing, [])

    def test_internal_markdown_links_resolve_to_pages(self) -> None:
        missing: list[str] = []
        for page in PUBLIC.rglob("*.mdx"):
            source = page.read_text(encoding="utf-8")
            for route in re.findall(r"\]\((/[^)#?]+)", source):
                if route == "/":
                    continue
                target = PUBLIC / f"{route.lstrip('/')}.mdx"
                if not target.is_file():
                    missing.append(f"{page.relative_to(PUBLIC)} -> {route}")
        self.assertEqual(missing, [])
