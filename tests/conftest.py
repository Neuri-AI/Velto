"""Make the sibling source distributions available for facade contract tests."""

from __future__ import annotations

import sys
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parents[2]
for package in ("velto", "qyro", "psx", "pydux"):
    source = str(WORKSPACE / package)
    if source not in sys.path:
        sys.path.insert(0, source)
