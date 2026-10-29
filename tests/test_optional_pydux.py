"""Public facade can be imported without installing optional Pydux."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType


class PSXStub(ModuleType):
    def __getattr__(self, name):
        return name


def _load_ui(monkeypatch, pydux):
    monkeypatch.setitem(sys.modules, "psx", PSXStub("psx"))
    monkeypatch.setitem(sys.modules, "pydux", pydux)
    path = Path(__file__).parents[1] / "velto" / "ui" / "__init__.py"
    spec = importlib.util.spec_from_file_location("_velto_ui_optional_test", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_ui_facade_without_pydux(monkeypatch):
    ui = _load_ui(monkeypatch, None)
    assert "psx" in ui.__all__
    assert "Native" in ui.__all__
    assert "native_adapter" in ui.__all__
    assert "Reactive" not in ui.__all__
    assert "connect" not in ui.__all__


def test_ui_facade_with_optional_pydux(monkeypatch):
    fake = ModuleType("pydux")
    for name in ("MainThreadBridge", "Reactive", "ReactiveBinding", "connect", "connect_qyro"):
        setattr(fake, name, name)
    ui = _load_ui(monkeypatch, fake)
    assert "Reactive" in ui.__all__
    assert ui.connect == "connect"
    assert ui.native_adapter == "native_adapter"
