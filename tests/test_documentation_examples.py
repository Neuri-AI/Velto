"""Smoke tests for the executable documentation projects."""
from __future__ import annotations

import runpy
import sys
import unittest
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parents[2]
for package in ("velto", "qyro", "psx", "pydux"):
    source = str(WORKSPACE / package)
    if source not in sys.path:
        sys.path.insert(0, source)

from psx.core.reconcile import Reconciler  # noqa: E402
from psx.renderers.headless import HeadlessRenderer  # noqa: E402
from psx.sfle.engine import PythonLayoutEngine  # noqa: E402
from psx.sfle.model import AvailableSize, IntrinsicSizes, LayoutConstraints  # noqa: E402


ROOT = Path(__file__).resolve().parents[1] / "examples" / "documentation" / "focusboard"
STAGES = (
    "stage-01-hello", "stage-02-components", "stage-03-interaction", "stage-04-dynamic-ui",
    "stage-05-layout", "stage-06-shared-state", "stage-07-runtime",
)


class FocusBoardExampleTests(unittest.TestCase):
    def test_focusboard_stages_build_mountable_trees(self) -> None:
        for stage in STAGES:
            with self.subTest(stage=stage):
                namespace = runpy.run_path(str(ROOT / stage / "main.py"))
                renderer = HeadlessRenderer(
                    sfle_constraints=LayoutConstraints(AvailableSize(640, True), AvailableSize(480, True)),
                    engine=PythonLayoutEngine(),
                    measure_intrinsic=lambda node: IntrinsicSizes(4, 20, 8, 12, 18, 12, 8),
                )
                reconciler = Reconciler(renderer)
                self.assertIsNotNone(reconciler.render(namespace["build"]()).native_handle())
                reconciler.unmount()
                if stage == "stage-05-layout":
                    self.assertEqual(namespace["grid_layout"]().type, "Grid")

    def test_distribution_stage_records_the_known_reproducibility_blocker(self) -> None:
        evidence = (ROOT / "stage-08-distribution" / "README.md").read_text(encoding="utf-8")
        self.assertIn("without declaring it", evidence)
