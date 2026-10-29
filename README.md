# Velto

Velto is the public application facade for Qyro, PSX, and Pydux.

```python
from velto import VeltoContext
from velto.ui import Flex, Text, psx
from velto.ui import Native, native_adapter
# Optional: from velto.state import configure_store, create_slice
from velto.runtime import get_resource, is_frozen
```

Velto reexports existing public APIs directly. Projects that import from
`qyro`, `psx`, or `pydux` remain supported and interoperate with Velto.

See [the public API contract](docs/public-api.md) and
[the compatibility matrix](docs/compatibility.md).


Pydux is **optional**. Install `velto[state]` to use the Pydux-backed
`velto.state` APIs; regular PSX Markup, `use_state` and `Native` work
without Pydux. Native reactive widget integration uses
`<Native widget={Widget} props={{"value": value}} />` together with
`update_props(self, props, changed)` or `@native_adapter(Widget)`.
See [the facade contract](docs/public-api.md).
