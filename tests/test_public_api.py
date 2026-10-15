"""The Velto facade must preserve the identity of approved public APIs."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_root_is_minimal_and_does_not_load_domain_namespaces() -> None:
    workspace = Path(__file__).resolve().parents[2]
    paths = [workspace / name for name in ("velto", "qyro", "psx", "pydux")]
    code = "import sys, velto; assert 'velto.ui' not in sys.modules; assert 'velto.state' not in sys.modules"
    result = subprocess.run(
        [sys.executable, "-c", code],
        env={"PYTHONPATH": ":".join(map(str, paths))},
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr


def test_root_reexports_qyro_context_without_a_wrapper() -> None:
    import qyro
    import velto

    assert velto.__all__ == ["VeltoContext", "__version__"]
    assert velto.VeltoContext is qyro.VeltoContext
    assert velto.VeltoContext.__module__ == "qyro.client.velto_context"


def test_domain_reexports_are_the_original_objects() -> None:
    import psx
    import pydux
    import qyro
    from psx.integrations.pydux import StoreProvider, use_dispatch, use_selector
    from psx.integrations.qyro import PSXMount, QyroProvider, mount_psx
    from velto import runtime, state, ui

    assert ui.Button is psx.Button
    assert ui.ComponentRegistry is psx.ComponentRegistry
    assert ui.register_adapter is psx.register_adapter
    assert ui.PSXMount is PSXMount
    assert ui.QyroProvider is QyroProvider
    assert ui.mount_psx is mount_psx
    assert ui.StoreProvider is StoreProvider
    assert ui.use_dispatch is use_dispatch
    assert ui.use_selector is use_selector
    assert state.Store is pydux.Store
    assert state.configure_store is pydux.configure_store
    assert runtime.EngineContainer is qyro.EngineContainer
    assert runtime.get_resource is qyro.get_resource


def test_public_surfaces_are_closed() -> None:
    from velto import runtime, state, ui

    assert set(state.__all__) == {
        "Action", "Dispatch", "Middleware", "PyDuxDevTools", "PyDuxInspectorServer", "Reducer",
        "Selector", "Slice", "Store", "combine_reducers", "configure_store",
        "create_async_thunk", "create_selector", "create_slice", "create_thunk_middleware",
        "deep_equal", "devtools_middleware", "is_identical", "shallow_equal", "start_inspector",
    }
    assert {"PSXMount", "QyroProvider", "StoreProvider", "use_selector", "load_plugins"} <= set(ui.__all__)
    assert {"EngineContainer", "get_resource", "is_frozen"} <= set(runtime.__all__)
