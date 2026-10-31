<p align="center">
  <img
    src="https://ik.imagekit.io/kummiktgaiq/ppg/velto-logo_KcLcXCZnT.png"
    alt="velto Logo"
    width="50%"
  >
</p>

# Velto

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://python.org)
[![velto Platforms Tests](https://github.com/Neuri-AI/velto/actions/workflows/matrix.yml/badge.svg)](https://github.com/Neuri-AI/velto/actions/workflows/matrix.yml)
![GitHub Release](https://img.shields.io/github/v/release/Neuri-AI/velto?include_prereleases&display_name=release&color=stable)
![GitHub Issues](https://img.shields.io/github/issues/Neuri-AI/velto)
![GitHub Issues Closed](https://img.shields.io/github/issues-closed/Neuri-AI/velto?color=green)
![GitHub forks](https://img.shields.io/github/forks/Neuri-AI/velto)
![GitHub stars](https://img.shields.io/github/stars/Neuri-AI/velto)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Sponsor](https://img.shields.io/badge/Sponsor-Buy%20Me%20a%20Coffee-FFDD00?logo=buymeacoffee&logoColor=000000)](https://buymeacoffee.com/neuri)

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
