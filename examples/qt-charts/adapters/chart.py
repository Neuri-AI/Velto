
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCharts import (
    QChart,
    QChartView,
    QLineSeries,
)
from velto.ui import native_adapter


@native_adapter(QChartView)
def update_chart(widget, props, changed):
    if "values" not in changed:
        return

    values = props["values"]

    # Initialize the chart once per native widget.
    series = getattr(widget, "_velto_series", None)

    if series is None:
        chart = QChart()
        chart.setTitle("Velto · Live data")
        chart.setAnimationOptions(
            QChart.AnimationOption.SeriesAnimations
        )
        chart.setBackgroundBrush(QColor("#ffffff"))

        series = QLineSeries()
        series.setName("Activity")
        series.setColor(QColor("#39ECC1"))

        chart.addSeries(series)
        chart.createDefaultAxes()

        widget.setChart(chart)
        widget.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        widget._velto_series = series

    # Update data without recreating QChartView.
    series.clear()

    for index, value in enumerate(values):
        series.append(float(index), float(value))

    # Adjust the visible axes.
    chart = widget.chart()

    if chart.axes(Qt.Orientation.Horizontal):
        x_axis = chart.axes(
            Qt.Orientation.Horizontal
        )[0]
        x_axis.setRange(0, max(1, len(values) - 1))

    if chart.axes(Qt.Orientation.Vertical):
        y_axis = chart.axes(
            Qt.Orientation.Vertical
        )[0]
        y_axis.setRange(
            0,
            max(10, max(values, default=0) + 2)
        )