
import sys

from velto import VeltoContext
from velto.ui import psx, use_state, use_ref
from velto.runtime import get_resource
from utils.address_solver import resolve_address


class WebviewApp(VeltoContext):

    def render(self):
        initial_url = "https://google.com"

        render_html, set_render_html = use_state(False)

        browser, set_browser = use_state({
            "address": initial_url,
            "url": initial_url,
        })

        webview_ref = use_ref(None)

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
            if webview_ref.current is not None:
                webview_ref.current.back()

        def handle_forward():
            if webview_ref.current is not None:
                webview_ref.current.forward()

        def handle_reload():
            if webview_ref.current is not None:
                webview_ref.current.reload()

        return psx("""
            <>
                <link rel="stylesheet" href="css/styles.css"/>

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

                    <Webview
                        ref={webview_ref}
                        src={render_html ? html : browser.url}
                        class="webview"
                    />
                </div>
            </>
        """)


if __name__ == "__main__":
    sys.exit(WebviewApp().run())
