# Public API

| Velto namespace | Source library | Public responsibility |
| --- | --- | --- |
| `velto` | Qyro | Application entry point: `VeltoContext` |
| `velto.ui` | PSX and public visual bridges | UI, components, hooks, rendering, plugins, adapters, and providers |
| `velto.state` | Pydux | Stores, reducers, selectors, middleware, and devtools |
| `velto.runtime` | Qyro | Resources, settings, execution environment, platform, and runtime errors |

`velto.ui` also exposes the approved public integration APIs: `PSXMount`,
`QyroProvider`, `mount_psx`, `use_container`, `use_qyro_context`,
`use_resource`, `use_settings`, `StoreProvider`, `use_dispatch`, and
`use_selector`.

The facade has no wrappers: `velto.ui.Button is psx.Button`,
`velto.state.Store is pydux.Store`, and `velto.VeltoContext is qyro.VeltoContext`.
Original imports remain part of each library's supported API.
