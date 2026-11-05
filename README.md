<p align="center">
  <img src="https://ik.imagekit.io/kummiktgaiq/ppg/velto-logo_KcLcXCZnT.png" alt="Velto logo" width="45%" />
</p>

# Velto
Build native applications in Python with declarative, reactive interfaces

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue.svg)](https://python.org)
[![velto Platforms Tests](https://github.com/Neuri-AI/velto/actions/workflows/matrix.yml/badge.svg)](https://github.com/Neuri-AI/velto/actions/workflows/matrix.yml)
![GitHub Release](https://img.shields.io/github/v/release/Neuri-AI/velto?include_prereleases&display_name=release&color=stable)
![GitHub Issues](https://img.shields.io/github/issues/Neuri-AI/velto)
![GitHub Issues Closed](https://img.shields.io/github/issues-closed/Neuri-AI/velto?color=green)
![GitHub forks](https://img.shields.io/github/forks/Neuri-AI/velto)
![GitHub stars](https://img.shields.io/github/stars/Neuri-AI/velto)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Sponsor](https://img.shields.io/badge/Sponsor-Buy%20Me%20a%20Coffee-FFDD00?logo=buymeacoffee&logoColor=000000)](https://buymeacoffee.com/neuri)


Velto is a Python framework for building native graphical applications using declarative components, reactive state, and a shared layout engine. It combines a Python-first development experience with native rendering through Qt, Tkinter, and Kivy—without requiring a web browser for the UI.


> **Project status:** Velto 0.1.x is an early-stage release. APIs, tooling, backend parity, and mobile deployment are actively evolving. Desktop support and mobile deployment have different levels of maturity.

## Highlights

- **Declarative Python UI:** Describe interfaces with PSX markup.
- **Reactive updates:** Build stateful components using hooks such as `use_state`, `use_effect`, and `use_ref`.
- **Native backends:** Render through Qt, Tkinter, and Kivy.
- **Styling and layout:** Use HTML-like elements, CSS-like styles, Flex, Grid, and scrolling primitives.
- **Native integration:** Embed toolkit widgets using `Native` and extend reactive updates through adapters.
- **Global state:** Integrate Pydux when local component state is not enough.
- **CLI:** Use the Velto CLI for project setup, execution, and packaging workflows.

## Quick start

The **recommended way to create, run, and package a Velto application is through [Velto CLI](https://github.com/Neuri-AI/Velto-CLI)**. It initializes the project structure, configures the selected native framework, and provides a consistent development and release workflow.

### 1. Install the CLI

Use a supported Python installation (Python 3.10–3.14 is a conservative choice; compatibility depends on package versions and the selected backend). A virtual environment is recommended:

```bash
python -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Or on Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Then install the desktop tooling:

```bash
python -m pip install --upgrade pip
python -m pip install "velto-cli[desktop]"
```

### 2. Create your application

```bash
velto init --name my-app
```

The interactive setup guides you through the available frameworks and project options. To select PySide6 explicitly:

```bash
velto init --name my-app --framework pyside6
```

Velto CLI supports desktop framework choices including **PySide6, PyQt6, PyQt5, PySide2, Kivy, and Tkinter**, subject to their platform and Python compatibility.

### 3. Start developing

```bash
cd my-app
velto start
```

Edit the generated `main.py` and other project files. For example, a simple reactive component looks like this:

```python
import sys
from velto import VeltoContext
from velto.ui import psx, use_state


class CounterApp(VeltoContext):
    def render(self):
        count, set_count = use_state(0)

        return psx("""
            <div style="display: flex; flex-direction: column; gap: 16px; padding: 24px;">
                <h1>Hello, Velto!</h1>
                <p>Build reactive native interfaces with Python.</p>
                <button on_click={() => set_count(count + 1)}>
                    Count is {count}
                </button>
            </div>
        """)


if __name__ == "__main__":
    sys.exit(CounterApp().run())
```

The example shows component-local reactive state. PSX updates the affected UI nodes and the selected backend renders the native widgets. Run the application using **`velto start`** from the project directory.

For a complete starter project with stylesheets and assets, see [examples/hello-world](examples/hello-world).

### 4. Build and distribute

From the project directory, build your desktop application:

```bash
velto build
```

To produce a single executable, where supported:

```bash
velto build --onefile
```

For distribution, use the CLI's platform-aware packaging workflow:

```bash
velto bundle
```

The CLI also provides signing and release tools. See the [Velto CLI documentation](https://github.com/Neuri-AI/Velto-CLI) for packaging formats, settings, prerequisites, and platform-specific behavior.

> [!NOTE]
> Velto CLI is in alpha. Desktop development is the supported workflow; Android and iOS packaging are experimental and should not be treated as production-ready.

## Architecture

Velto exposes one application-facing interface while preserving clear responsibilities for each subsystem:

```text
                        Your Python application
                                  |
                           velto (facade)
                                  |
                +-----------------+----------------+
                |                 |                |
           Qyro Engine           PSX          Pydux (optional)
          Runtime/lifecycle   UI + reactivity    Shared state
                                  |
                               Cinnamon
                           Layout geometry
                                  |
                       Native renderer adapters
                                  |
                        Qt / Tkinter / Kivy
```

| Component | Responsibility | Repository |
| --- | --- | --- |
| **Velto** | Public application-facing imports | [Neuri-AI/Velto](https://github.com/Neuri-AI/Velto) |
| **Qyro Engine** | Application lifecycle, runtime services, and resource handling | [Neuri-AI/qyro](https://github.com/Neuri-AI/qyro) |
| **PSX / Velto Core** | Declarative markup, components, reconciliation, hooks, and native adapters | [Neuri-AI/PSX](https://github.com/Neuri-AI/PSX) |
| **Cinnamon** | Shared geometric layout computation used by PSX | [Neuri-AI/PSX](https://github.com/Neuri-AI/PSX) |
| **Pydux** | Optional store, reducers, selectors, and state integration | [Neuri-AI/Pydux](https://github.com/Neuri-AI/Pydux) |
| **Velto CLI** | Project development and packaging commands | [Neuri-AI/Velto-CLI](https://github.com/Neuri-AI/Velto-CLI) |

### What happens when Velto renders?

1. Your `VeltoContext` provides the application entry point and lifecycle.
2. PSX processes markup and component definitions into a virtual UI representation.
3. Hooks and reconciliation track state changes and determine which nodes need updating.
4. Cinnamon computes the layout geometry for the UI.
5. The selected renderer maps the result to native toolkit widgets.

The UI is **not rendered as an HTML page inside a browser**. Explicit native integrations, such as a web view embedded in an application, are available separately.

## Unified public API

```python
from velto import VeltoContext
from velto.ui import psx, component, use_state, use_effect, use_ref
from velto.ui import Flex, Grid, GridItem, Scroll, Text, Native, native_adapter
from velto.runtime import get_resource, is_frozen

# Optional: requires `velto[state]`
from velto.state import configure_store, create_slice, use_dispatch, use_selector
```

Velto reexports the underlying libraries' public objects rather than maintaining a separate wrapper implementation. Existing applications importing from `qyro`, `psx`, or `pydux` can continue using those APIs.

See the [public API reference](docs/public-api.md) for the facade contract and integration details.

## Native widget integration

PSX can mount existing native widgets through the `Native` component. For reactive widget properties, use a widget-owned `update_props(self, props, changed)` method or register an adapter with `@native_adapter(WidgetType)`.

```python
from velto.ui import native_adapter

@native_adapter(MyWidget)
def update_my_widget(widget, props, changed):
    if "value" in changed:
        widget.set_value(props["value"])
```

```jsx
<Native widget={MyWidget} props={{"value": current_value}} />
```

Native widget construction parameters can also be passed separately. Refer to the [native integration contract](docs/public-api.md) before using toolkit-specific APIs.

## Examples

Explore the working examples in this repository:

| Example | Description |
| --- | --- |
| [Hello World](examples/hello-world) | Minimal reactive application |
| [Dashboard](examples/dashboard) | Multi-section application layout |
| [Pydux login screen](examples/pydux-login-screen) | Optional centralized state integration |
| [Qt Charts](examples/qt-charts) | Native chart integration |
| [Chromium browser](examples/chromium-browser) | Browser component embedded as a native integration |
| [WebView app](examples/webview-app) | Web view integration |
| [Third-party libraries](examples/third-party-libraries) | Extending applications with external UI libraries |

## Platforms and compatibility

Velto targets desktop applications on **Linux, Windows, and macOS**, depending on the selected backend and its available native dependencies.

Android and iOS are areas of ongoing development. Mobile packaging and deployment should not yet be assumed to have the same maturity or compatibility coverage as desktop.

The current repository's package manifest requires `Python >=3.10,<3.13.20`, while [docs/compatibility.md](docs/compatibility.md) describes a broader 0.1.x certification range. When choosing an installation environment, use the published package metadata and the constraints of your selected backend as the source of truth.

## Development workflow

The [Velto CLI](https://github.com/Neuri-AI/Velto-CLI) provides commands for generating and working with projects:

```bash
velto init
velto start
```

CLI installation, backend selection, and build options are documented in the CLI repository. Packaging and mobile build support vary by platform and backend.

To contribute to this facade repository:

```bash
git clone https://github.com/Neuri-AI/Velto.git
cd Velto
python -m pip install -e ".[pyside6]"
python -m pip install pytest
python -m pytest
```

Some integration tests may require additional backend packages or platform-specific tools.

## Documentation

- [Public API and native integration](docs/public-api.md)
- [Compatibility matrix](docs/compatibility.md)
- [PSX source and documentation](https://github.com/Neuri-AI/PSX)
- [Qyro Engine](https://github.com/Neuri-AI/qyro)
- [Velto CLI](https://github.com/Neuri-AI/Velto-CLI)
- [Examples](examples)

## Contributing

Contributions, reproducible bug reports, and documentation improvements are welcome. Before submitting a change, review the relevant subsystem repository, provide a minimal reproduction for defects, and run the applicable test suite.

Open an [issue](https://github.com/Neuri-AI/Velto/issues) for facade-level bugs or feature discussions.

## License

Velto is released under the [MIT License](LICENSE). Individual runtime engines, UI bindings, and other dependencies may have their own license obligations; consult [NOTICE](NOTICE) and the corresponding upstream packages.
