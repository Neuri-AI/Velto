"""Packaged native application with genuine Qyro protected-resource access."""
from pathlib import Path

from velto import VeltoContext
from velto.ui import psx


class PackagedApplication(VeltoContext):
    def render(self):
        return psx('<Flex width="320px" height="120px"><Text value="Frozen integration" /></Flex>')


def main():
    application = PackagedApplication(enable_sentry=False)
    try:
        application.mount()
        assert application.is_frozen, "Certification must execute the PyInstaller binary"
        assert application.metadata.app_name == "VeltoFrozenSmoke"
        path = Path(application.get_resource("fixtures", "token.txt"))
        assert path.read_text(encoding="utf-8") == "protected-by-qyro"
        application.renderer.root.after(75, application.renderer.root.quit)
        result = application.run()
        assert result in (None, 0)
        print("VELTO_FROZEN_RESOURCE_AND_WINDOW_OK", flush=True)
    finally:
        application.unmount()


if __name__ == "__main__":
    main()
