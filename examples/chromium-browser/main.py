
import sys
from pathlib import Path
from velto import VeltoContext
from velto.ui import (
    psx,
    use_state,
    use_ref
)
from velto.runtime import get_resource
from utils.address_solver import resolve_address
from adapters.chromium_adapters import update_browser
from PySide6.QtWebEngineWidgets import QWebEngineView

class ChromiumBrowser(VeltoContext):

    def render(self):
        initial_url = "https://google.com"

        render_html, set_render_html = use_state(False)

        browser, set_browser = use_state({
            "address": initial_url,
            "url": initial_url,
        })

        chromium_ref = use_ref(None)

        html = get_resource("html/index.html")

        def handle_address_change(event):
            set_browser({
                **browser,
                "address": event.target.value,
            })

        def handle_navigate():
            url = resolve_address(browser["address"])

            if not url:
                return

            set_browser({
                "address": url,
                "url": url,
            })

        def handle_back():
            if chromium_ref.current is not None:
                chromium_ref.current.back()

        def handle_forward():
            if chromium_ref.current is not None:
                chromium_ref.current.forward()

        def handle_reload():
            if chromium_ref.current is not None:
                chromium_ref.current.reload()

        def handle_url_changed(url):
            # Update the address bar without triggering
            # a second navigation.
            address = url.toString()

            if address and address != browser["address"]:
                set_browser({
                    **browser,
                    "address": address,
                })

        browser_props = {
            "src": html if render_html else browser["url"]
        }

        browser_signals = {
            "urlChanged": handle_url_changed
        }

        return psx("""
            <>
                <link rel="stylesheet"
                      href="css/styles.css"/>

                <div class="root">
                    <div class="header">

                        <div class="navigation">
                            <button on_click={handle_back}>
                                ←
                            </button>

                            <button on_click={handle_forward}>
                                →
                            </button>

                            <button on_click={handle_reload}>
                                ↻
                            </button>
                        </div>

                        <form
                            class="address-bar"
                            on_submit={handle_navigate}
                        >
                            <input
                                type="text"
                                placeholder="Search or enter URL"
                                value={browser.address}
                                on_change={handle_address_change}
                            />
                        </form>

                        <div class="switch-row">
                            <Switch
                                checked={render_html}
                                on_change={set_render_html}
                            />
                            <span>Render static file</span>
                        </div>
                    </div>

                    <Native
                        widget={QWebEngineView}
                        props={browser_props}
                        signals={browser_signals}
                        ref={chromium_ref}
                        class="browser"
                    />
                </div>
            </>
        """)


if __name__ == "__main__":
    sys.exit(ChromiumBrowser().run())
