import sys
from velto import VeltoContext
from velto.ui import psx, use_state

from adapters.chart import QChartView, update_chart

class QtCharts(VeltoContext):

    def render(self):
        count, set_count = use_state(0)
        values, set_values = use_state([3, 6, 4, 9, 7])

        chart_props = {
            "values": tuple(values)
        }

        def handle_add_data():
            set_count(count + 1)
            set_values([
                *values,
                values[-1] + (3 if count % 2 == 0 else -1)
            ])

        return psx("""
            <>
                <link rel="stylesheet" href="css/styles.css"/>

                <div class="root">
                    <h1>Qt Charts + Velto</h1>
                    <Native
                        widget={QChartView}
                        props={chart_props}
                        width="100%"
                        height="360px"
                    />

                    <button on_click={handle_add_data}>
                        Add data ({count})
                    </button>

                    <a href="https://getvelto.dev">
                        Explore the docs
                    </a>
                </div>
            </>
        """)


if __name__ == "__main__":
    sys.exit(QtCharts().run())
