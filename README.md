# Velto

Velto is the public application facade for Qyro, PSX, and Pydux.

```python
from velto import VeltoContext
from velto.ui import Flex, Text, psx
from velto.state import configure_store, create_slice
from velto.runtime import get_resource, is_frozen
```

Velto reexports existing public APIs directly. Projects that import from
`qyro`, `psx`, or `pydux` remain supported and interoperate with Velto.

See [the public API contract](docs/public-api.md) and
[the compatibility matrix](docs/compatibility.md).
