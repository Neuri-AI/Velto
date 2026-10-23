"""Sustained mounted Tkinter state and resource ownership certification."""
from __future__ import annotations

import json
import os
from pathlib import Path
import sys
import tracemalloc

import psutil

from velto import VeltoContext
from velto.ui import psx
from velto.state import Action, Store, use_selector


def reducer(state, action):
    if action.type == "advance":
        return {"count": state["count"] + 1}
    return state


def test_sustained_native_state_updates_release_resources(tmp_path):
    settings_dir = tmp_path / "settings"
    settings_dir.mkdir()
    (settings_dir / "base.json").write_text(json.dumps({
        "app_name": "Sustained native runtime",
        "framework": "tkinter",
        "window": {"width": 320, "height": 120},
    }), encoding="utf-8")

    store = Store(reducer, {"count": 0})
    observed = []

    class Application(VeltoContext):
        pydux_store = store

        def render(self):
            count = use_selector(lambda state: state["count"])
            observed.append(count)
            return psx(
                '<Flex width="320px" height="120px"><Text value={text} /></Flex>',
                scope={"text": str(count)},
            )

    process = psutil.Process()
    previous_container = VeltoContext._global_container
    previous_boot = VeltoContext._global_boot_info
    previous_hook = sys.excepthook
    VeltoContext._global_container = None
    VeltoContext._global_boot_info = None
    samples = []
    app = None
    tracemalloc.start()
    try:
        app = Application(custom_root=tmp_path, enable_sentry=False)
        app.mount()
        for index in range(2000):
            store.dispatch(Action("advance"))
            app.renderer.root.update()
            if index % 100 == 99:
                current, _peak = tracemalloc.get_traced_memory()
                samples.append({
                    "iteration": index + 1,
                    "rss_bytes": process.memory_info().rss,
                    "python_bytes": current,
                })
        assert observed[-1] == 2000
        assert store.get_state() == {"count": 2000}
        assert len(samples) == 20
        start, end = samples[3], samples[-1]
        assert end["rss_bytes"] - start["rss_bytes"] < 64 * 1024 * 1024
        assert end["python_bytes"] - start["python_bytes"] < 12 * 1024 * 1024
        report_dir = Path(os.environ.get("VELTO_RESOURCE_REPORT_DIR", tmp_path))
        report_dir.mkdir(parents=True, exist_ok=True)
        (report_dir / "sustained-state.json").write_text(
            json.dumps({"backend": "tkinter", "engine": os.environ.get("EXPECTED_LAYOUT_ENGINE"),
                        "samples": samples, "observed_updates": observed[-1]}, indent=2),
            encoding="utf-8",
        )
    finally:
        if app is not None:
            app.unmount()
            assert app.handle is None
            assert getattr(store, "_pydux_psx_inspector_leases", 0) == 0
        tracemalloc.stop()
        VeltoContext._global_container = previous_container
        VeltoContext._global_boot_info = previous_boot
        sys.excepthook = previous_hook
