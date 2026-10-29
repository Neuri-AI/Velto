# Public API

| Velto namespace | Source library | Public responsibility |
| --- | --- | --- |
| `velto` | Qyro | Application entry point: `VeltoContext` |
| `velto.ui` | PSX | UI, components, hooks, rendering, plugins, and adapters |
| `velto.state` | Pydux | Stores, reducers, selectors, middleware, devtools, and PSX state hooks |
| `velto.runtime` | Qyro | Resources, settings, execution environment, platform, and runtime errors |

`velto.state` exposes the Pydux PSX integration APIs: `StoreProvider`,
`use_dispatch`, and `use_selector`. Qyro/Velto applications use
`velto.VeltoContext`; the facade does not expose a separate PSX↔Qyro bridge.
When a `VeltoContext` view module declares one Pydux store, the context applies
`StoreProvider` automatically, so hooks can be called directly from `render()`.

The facade has no wrappers: `velto.ui.Button is psx.Button`,
`velto.state.Store is pydux.Store`, and `velto.VeltoContext is qyro.VeltoContext`.
Original imports remain part of each library's supported API.

## Native reactive widgets

`velto.ui` reexports `Native` and `native_adapter` from PSX. Unmodified
toolkit widgets can be mounted with `<Native widget={QWebEngineView} />`,
without an update handler.

To send reactive values, add a `props` mapping. An owned custom class can
define `update_props(self, props, changed)`, where `changed` is a
`frozenset[str]` of changed keys; for external classes use
`@native_adapter(WidgetType)` with signature
`(widget, props, changed)`. Widget-owned `update_props` takes precedence.
`kwargs` (and optionally `args`) are for construction only, and changing
their values triggers remount of the native widget. Layout remains Cinnamon-owned.

```python
from velto.ui import native_adapter

@native_adapter(QWebEngineView)
def update_browser(widget, props, changed):
    if "url" in changed:
        widget.setUrl(QUrl(props["url"]))
```

```jsx
<Native widget={QWebEngineView}
        props={{"url": current_url}}
        width="100%" height="100vh" key="browser" />
```

See the complete PSX reference:
[Native reactive props](https://github.com/Neuri-AI/PSX/blob/fixes/psx-issues/docs/native-reactive-props.md).

## Optional Pydux state integration

Core `velto` and `velto.ui` do **not** require Pydux. Install
`velto[state]` to enable `velto.state` and the Pydux-specific
`MainThreadBridge`, `Reactive`, `ReactiveBinding`, `connect` and
`connect_qyro` exports from `velto.ui`. Importing `velto.state`
without Pydux installed is unsupported; the rest of the façade remains usable.
