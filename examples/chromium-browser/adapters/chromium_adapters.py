from pathlib import Path
from PySide6.QtWebEngineWidgets import QWebEngineView
from velto.ui import native_adapter
from utils.address_solver import resolve_chromium_url

@native_adapter(QWebEngineView)
def update_browser(widget, props, changed):
    if "src" not in changed:
        return

    source = props.get("src")

    if not source:
        widget.setHtml("")
        return

    url = resolve_chromium_url(source)

    if url.isLocalFile():
        path = Path(url.toLocalFile())

        if path.suffix.lower() in (".html", ".htm"):
            content = path.read_text(encoding="utf-8-sig")
            widget.setHtml(content, url)
        else:
            widget.load(url)
    else:
        widget.load(url)