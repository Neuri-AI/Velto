
import os
import pyqtgraph as pg
from velto.ui import native_adapter
os.environ.setdefault("PYQTGRAPH_QT_LIB", "PySide6")
PlotWidget = pg.PlotWidget


@native_adapter(PlotWidget)
def update_chart(widget, props, changed):
    """
    Adaptador reactivo para PyQtGraph.

    El gráfico se inicializa una sola vez.
    Las actualizaciones posteriores modifican las series
    existentes sin recrear el widget.
    """
    if not hasattr(widget, "_velto_curves"):
        widget.setBackground("#141820")

        plot = widget.getPlotItem()

        plot.setTitle(
            "Live Metrics",
            color="#FFFFFF",
            size="16pt",
        )

        plot.setLabel("left", "Value")
        plot.setLabel("bottom", "Sample")

        plot.showGrid(
            x=True,
            y=True,
            alpha=0.2,
        )

        plot.addLegend()

        plot.setClipToView(True)
        plot.setDownsampling(
            auto=True,
            mode="peak",
        )

        primary = plot.plot(
            [],
            [],
            name="Primary",
            pen=pg.mkPen("#39ECC1", width=2),
        )

        # Serie secundaria.
        secondary = plot.plot(
            [],
            [],
            name="Secondary",
            pen=pg.mkPen("#6495FF", width=2),
        )

        widget._velto_curves = {
            "primary": primary,
            "secondary": secondary,
        }

    for name in ("primary", "secondary"):
        if name not in changed:
            continue

        values = props.get(name, ())
        curve = widget._velto_curves[name]

        curve.setData(
            x=list(range(len(values))),
            y=list(values),
        )
