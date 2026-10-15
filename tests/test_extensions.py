"""Third-party extensions use the same PSX objects through ``velto.ui``."""

from __future__ import annotations


def test_component_library_uses_the_original_registry() -> None:
    import psx
    from velto import ui

    registry = ui.ComponentRegistry()
    definition = ui.register_component(registry, "Banner", ui.Text, namespace="acme")

    assert ui.ComponentRegistry is psx.ComponentRegistry
    assert registry.resolve("acme.Banner") is definition
    assert definition.constructor is psx.Text


def test_plugin_registers_components_and_renderer_adapters() -> None:
    from psx.renderers.headless import HeadlessRenderer
    from velto import ui

    registry = ui.ComponentRegistry()
    renderer = HeadlessRenderer()
    adapter = object()

    class ExternalPlugin:
        def register(self, api: object) -> None:
            api.component("Banner", ui.Text)
            api.adapter("headless", "Banner", adapter)

    loaded = ui.load_plugins(
        registry,
        renderers={"headless": renderer},
        plugins=[ExternalPlugin()],
        namespace="acme",
    )

    assert len(loaded) == 1
    assert registry.resolve("acme.Banner").constructor is ui.Text
    assert renderer.adapters.get("acme.Banner") is adapter
    assert ui.renderer_capabilities(renderer).components >= {"acme.Banner"}


def test_psx_extensions_interoperate_with_velto_app_imports() -> None:
    import psx
    from velto import ui

    registry = psx.ComponentRegistry()
    psx.register_component(registry, "Chip", psx.Text, namespace="vendor")

    assert ui.ComponentRegistry is psx.ComponentRegistry
    assert registry.resolve("vendor.Chip").constructor is ui.Text
