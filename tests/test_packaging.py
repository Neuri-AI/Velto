"""Distribution metadata records the certified compatibility contract."""

from __future__ import annotations

import tomllib
from pathlib import Path


def test_distribution_metadata_declares_the_facade_dependency_graph() -> None:
    metadata = tomllib.loads((Path(__file__).parents[1] / "pyproject.toml").read_text())
    project = metadata["project"]

    assert project["name"] == "velto"
    assert project["requires-python"] == ">=3.10,<3.14"
    assert project["dependencies"] == [
        "qyro-engine>=0.1.0,<0.2.0",
        "psx>=1.0.0a1,<2.0.0",
        "pydux>=1.0.0a1,<2.0.0",
    ]
    assert set(project["optional-dependencies"]) == {
        "pyside6", "pyqt6", "pyqt5", "pyside2", "kivy", "sentry"
    }


def test_optional_qyro_integrations_use_the_certified_qyro_range() -> None:
    workspace = Path(__file__).resolve().parents[2]
    psx = tomllib.loads((workspace / "psx" / "pyproject.toml").read_text())
    pydux = tomllib.loads((workspace / "pydux" / "pyproject.toml").read_text())

    assert psx["project"]["optional-dependencies"]["qyro"] == [
        "qyro-engine>=0.1.0,<0.2.0"
    ]
    assert pydux["project"]["optional-dependencies"]["qyro"] == [
        "qyro-engine>=0.1.0,<0.2.0"
    ]
