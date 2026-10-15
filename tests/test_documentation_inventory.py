"""Keep declared documentation coverage synchronized with the façade contract."""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
for package in ("velto", "qyro", "psx", "pydux"):
    source = str(WORKSPACE / package)
    if source not in sys.path:
        sys.path.insert(0, source)

import velto  # noqa: E402
from velto import runtime, state, ui  # noqa: E402


class DocumentationInventoryTests(unittest.TestCase):
    def test_inventory_matches_every_public_facade_export(self) -> None:
        inventory = json.loads((WORKSPACE / "public" / "_ops" / "api-inventory.json").read_text())
        documented = inventory["namespaces"]
        self.assertEqual(set(documented["velto"]), {"VeltoContext", "__version__"})
        self.assertEqual(set(documented["velto.runtime"]), set(runtime.__all__))
        self.assertEqual(set(documented["velto.state"]), set(state.__all__))
        self.assertEqual(set(documented["velto.ui"]), set(ui.__all__))

    def test_component_exports_have_individual_reference_pages(self) -> None:
        components = {"Badge", "Button", "Checkbox", "Divider", "Flex", "Fragment", "Grid", "GridItem", "Image", "Input", "Link", "Native", "ProgressBar", "Radio", "RadioGroup", "Scroll", "Select", "Slider", "Spacer", "SpinBox", "Switch", "Text", "TextArea"}
        directory = WORKSPACE / "public" / "reference" / "ui" / "components"
        slugs = {path.stem.replace("-", " ").title().replace(" ", "") for path in directory.glob("*.mdx")}
        self.assertEqual(slugs, components)
