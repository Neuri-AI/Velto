
import sys
import math

from velto import VeltoContext
from velto.ui import psx, use_state
from adapters.pyqtgraph_chart import PlotWidget, update_chart


class ThirdPartyLibraries(VeltoContext):

    def render(self):
        initial_primary = tuple(
            50 + 20 * math.sin(i * 0.3)
            for i in range(30)
        )

        initial_secondary = tuple(
            40 + 15 * math.cos(i * 0.25)
            for i in range(30)
        )

        primary, set_primary = use_state(initial_primary)
        secondary, set_secondary = use_state(initial_secondary)
        show_secondary, set_show_secondary = use_state(True)

        chart_props = {
            "primary": primary,
            "secondary": secondary if show_secondary else (),
        }

        def handle_add_sample():
            index = len(primary)

            next_primary = (
                50 + 20 * math.sin(index * 0.3)
            )

            next_secondary = (
                40 + 15 * math.cos(index * 0.25)
            )

            set_primary((*primary, next_primary))
            set_secondary((*secondary, next_secondary))

        def handle_reset():
            set_primary(initial_primary)
            set_secondary(initial_secondary)

        return psx("""
            <>
                <link
                    rel="stylesheet"
                    href="css/styles.css"
                />

                <div class="root">
                    <h1>PyQtGraph + Velto</h1>

                    <p>
                        Samples: <span class="highlight">{len(primary)}</span>.
                    </p>

                    <div class="toolbar">
                        <button on_click={handle_add_sample}>
                            Add sample
                        </button>

                        <button on_click={handle_reset}>
                            Reset
                        </button>

                        <div class="switch-row">
                            <Switch
                                checked={show_secondary}
                                on_change={set_show_secondary}
                            />
                            <span>Secondary series</span>
                        </div>
                    </div>

<div class="chart-container">
    <Native
        widget={PlotWidget}
        props={chart_props}
        height="420px"
    />
</div>
                </div>
            </>
        """)


if __name__ == "__main__":
    sys.exit(ThirdPartyLibraries().run())
