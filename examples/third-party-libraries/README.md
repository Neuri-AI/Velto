# 🚀 Velto Desktop Boilerplate

> **The official, universal starter template for the [Velto](https://github.com/Neuri-AI/velto) framework.**

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://python.org)
[![Qt Bindings](https://img.shields.io/badge/UI-PySide6%20%7C%20PyQt6%20%7C%20PyQt5%20%7C%20PySide2-green.svg)](https://qt.io)
[![Kivy](https://img.shields.io/badge/UI-Kivy-green.svg)](https://kivy.org)
[![Tkinter](https://img.shields.io/badge/UI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

---

## Overview

`velto-boilerplate` is the default starter template used by `velto-cli` to scaffold production-ready applications in seconds. It provides zero-boilerplate window bootstrapping, reactive state management, and unified asset resolution across modern UI frameworks:

* **PySide2** (Qt 5 legacy)
* **PySide6** (Qt 6 official)
* **PyQt5** (Riverbank)
* **PyQt6** (Riverbank)
* **Kivy**
* **Tkinter**


---

## Features

* **Multi-Binding Support:** Run your app with any UI framework simply by editing your project settings.
* **Reactive State & Data-Binding:** Built-in event bus and reactive widget store out of the box.
* **Smart Resource Resolver:** Automated detection and loading of icons, images, and fonts (`resources/base/`, `resources/windows/`, `resources/mac/`, `resources/linux/`).
* **Desktop & Mobile Builds:** Pre-configured for standalone desktop executables via PyInstaller, with Android and iOS packaging support through Kivy and supported Qt toolchains.
* **Window Auto-Config:** Automatic application title and icons based on your configuration files.

---

## Usage

This template is scaffolded automatically via the **Velto CLI**:

```bash
# Create a project
velto init my-app
```

