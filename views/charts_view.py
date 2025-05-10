from PyQt6 import QtWidgets
from logic.charts import update_main_chart, update_comparison_chart, export_chart
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

def setup_charts_page(window):
    # Настройка графиков
    window.figure1 = Figure(figsize=(5, 4), dpi=100)
    window.canvas1 = FigureCanvas(window.figure1)
    layout1 = window.mainPlotContainer.layout() or QtWidgets.QVBoxLayout(window.mainPlotContainer)
    layout1.addWidget(window.canvas1)

    window.figure2 = Figure(figsize=(5, 4), dpi=100)
    window.canvas2 = FigureCanvas(window.figure2)
    layout2 = window.comparisonPlotContainer.layout() or QtWidgets.QVBoxLayout(window.comparisonPlotContainer)
    layout2.addWidget(window.canvas2)

    window.chartTypeCombo.clear()
    window.chartTypeCombo.addItems(["Столбчатая", "Ящик с усами", "Точечная"])

    window.chartTypeCombo.currentTextChanged.connect(lambda: update_main_chart(window))
    window.showTrendCheck.stateChanged.connect(lambda: update_main_chart(window))
    window.exportChartBtn.clicked.connect(lambda: export_chart(window))
    window.radioButton.toggled.connect(lambda: update_comparison_chart(window))
    window.radioButton_2.toggled.connect(lambda: update_comparison_chart(window))