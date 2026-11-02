from urllib.parse import quote_plus
from pathlib import Path
from PySide6.QtCore import QUrl

def resolve_address(text):
    text = text.strip()

    if not text:
        return None

    if text.startswith(("http://", "https://", "file://", "about:")):
        return text

    first = text.split("/", 1)[0]

    if (
        " " not in text
        and (
            "." in first
            or first.startswith("localhost")
            or first.startswith("127.0.0.1")
        )
    ):
        return f"http://{text}" if first.startswith(
            ("localhost", "127.0.0.1")
        ) else f"https://{text}"

    return f"https://www.google.com/search?q={quote_plus(text)}"

def resolve_chromium_url(source):
    if isinstance(source, QUrl):
        return source

    source = str(source).strip()

    # Preserve explicit URL schemes.
    url = QUrl(source)
    if not url.isRelative():
        return url

    # Convert local absolute paths to file:// URLs.
    path = Path(source).expanduser()
    if path.is_absolute() or source.startswith("~/"):
        return QUrl.fromLocalFile(str(path.absolute()))

    return QUrl(source)