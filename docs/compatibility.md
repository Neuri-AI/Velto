# Compatibility matrix

Velto 0.1.x is certified against the following distribution ranges:

| Distribution | Supported range |
| --- | --- |
| Python | `>=3.10,<3.14` |
| Qyro Engine | `>=0.1.0,<0.2.0` |
| PSX | `>=1.0.0a1,<2.0.0` |
| Pydux | `>=1.0.0a1,<2.0.0` |

The facade's CI validates imports, direct-export identity, public integration
APIs, third-party extension registration, and clean wheel installation for the
minimum versions and current compatible releases. Unsupported combinations are
excluded by these dependency bounds.
