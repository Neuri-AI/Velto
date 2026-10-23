"""Executable integration across the public facade, Qyro, Pydux, PSX and Cinnamon.

The only substituted boundary is native renderer selection, using PSX's REAL
headless renderer and real Python Cinnamon engine. No fake App/store/VNodes.
"""
from __future__ import annotations

import os

import pytest


def test_context_mounts_real_psx_cinnamon_and_pydux(monkeypatch):
    from velto import VeltoContext
    from velto.ui import psx
    from velto.state import Action, Store, use_selector
    from psx.renderers.headless import HeadlessRenderer
    from psx.sfle.engine import PythonLayoutEngine
    from psx.sfle.model import AvailableSize, LayoutConstraints
    from qyro.domain.entities import AppMetadata, ExecutionMode, PlatformType

    def reducer(state, action):
        if action.type == "increment":
            return {"count": state["count"] + 1}
        return state

    store = Store(reducer, {"count": 1})
    previous_container = VeltoContext._global_container
    previous_boot_info = VeltoContext._global_boot_info
    # The Qyro bootstrap environment is provided explicitly; everything from
    # VeltoContext.mount through the PSX app, layout and Pydux is real.
    VeltoContext._global_container = object()
    native_backend = os.environ.get("VELTO_INTEGRATION_BACKEND")
    VeltoContext._global_boot_info = {
        "metadata": AppMetadata(
            app_name="Integrated native application",
            raw_settings={"framework": native_backend or "tkinter", "window": {"width": 240, "height": 120}},
        ),
        "is_frozen": False,
        "platform": PlatformType.LINUX,
        "execution_mode": ExecutionMode.SOURCE,
    }

    def real_headless_renderer(_self, binding, width, height):
        assert binding == "tkinter"
        return HeadlessRenderer(
            sfle_constraints=LayoutConstraints(
                AvailableSize(width, True), AvailableSize(height, True)
            ),
            engine=PythonLayoutEngine(),
        )

    rendered_counts = []

    class IntegratedApplication(VeltoContext):
        pydux_store = store

        def render(self):
            count = use_selector(lambda state: state["count"])
            rendered_counts.append(count)
            return psx('<Flex width="240px" height="120px"><Text value={label} layout_width="90px" layout_height="20px" /></Flex>', scope={"label": f"Count {count}"})

    if native_backend is None:
        monkeypatch.setattr(IntegratedApplication, "_create_renderer", real_headless_renderer)
    monkeypatch.setattr(IntegratedApplication, "_present", lambda *_: None)
    instance = None
    try:
        instance = IntegratedApplication()
        native = instance.mount()
        assert native is instance.handle
        assert instance.app is not None
        assert instance.renderer.sfle_result is not None
        assert instance.renderer.sfle_result.geometry_commit_error == 0.0
        assert instance.mount() is native
        assert instance.app.reconciler is not None
        assert instance.pydux_store is store
        assert rendered_counts[-1] == 1
        store.dispatch(Action("increment"))
        instance.renderer.flush()
        assert store.get_state() == {"count": 2}
        assert rendered_counts[-1] == 2
    finally:
        if instance is not None:
            instance.unmount()
            assert instance.handle is None
            assert getattr(store, "_pydux_psx_inspector_leases", 0) == 0
        VeltoContext._global_container = previous_container
        VeltoContext._global_boot_info = previous_boot_info
