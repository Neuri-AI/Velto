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
