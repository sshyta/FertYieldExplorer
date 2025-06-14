from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.uic.properties import QtCore

from logic.charts import (
    update_main_chart, 
    update_comparison_chart, 
    export_chart,
    create_interaction_plot,
    create_heatmap
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

def setup_charts_page(window):
    """
    Настраивает страницу с графиками.
    
    Args:
        window: Главное окно приложения
    """
    # Настройка основного графика
    window.figure1 = Figure(figsize=(5, 4), dpi=100)
    window.canvas1 = FigureCanvas(window.figure1)
    layout1 = window.mainPlotContainer.layout() or QtWidgets.QVBoxLayout(window.mainPlotContainer)
    layout1.addWidget(window.canvas1)

    # Настройка графика сравнения
    window.figure2 = Figure(figsize=(5, 4), dpi=100)
    window.canvas2 = FigureCanvas(window.figure2)
    layout2 = window.comparisonPlotContainer.layout()
    if layout2 is None:
        layout2 = QtWidgets.QVBoxLayout(window.comparisonPlotContainer)
        window.comparisonPlotContainer.setLayout(layout2)
    layout2.addWidget(window.canvas2)


    # Подключение обработчика
    window.exportComparisonChartBtn.clicked.connect(lambda: export_chart(window))

    # Обновление списка типов графиков
    window.chartTypeCombo.clear()
    window.chartTypeCombo.addItems(["Столбчатая", "Точечная"])

    if window.chartsTabs.count() == 2:
        # === ВЗАИМОДЕЙСТВИЕ ===
        interaction_tab = QtWidgets.QWidget()
        window.chartsTabs.addTab(interaction_tab, "Взаимодействие")

        # Layout для всей вкладки
        interaction_layout = QtWidgets.QVBoxLayout(interaction_tab)

        # Контейнер и график
        window.figure3 = Figure(figsize=(10, 5), dpi=100)
        window.canvas3 = FigureCanvas(window.figure3)
        interaction_layout.addWidget(window.canvas3)

        # Кнопка обновления
        window.updateInteractionBtn = QtWidgets.QPushButton("Обновить график")
        interaction_layout.addWidget(window.updateInteractionBtn)

        window.exportInteractionBtn = QtWidgets.QPushButton("Экспорт графика")
        interaction_layout.addWidget(window.exportInteractionBtn)
        window.exportInteractionBtn.clicked.connect(lambda: export_chart(window))  # ✅ ДОБАВЬ ЭТО

        # === ТЕПЛОВАЯ КАРТА ===
        heatmap_tab = QtWidgets.QWidget()
        window.chartsTabs.addTab(heatmap_tab, "Тепловая карта")

        heatmap_layout = QtWidgets.QVBoxLayout(heatmap_tab)

        window.figure4 = Figure(figsize=(10, 5), dpi=100)
        window.canvas4 = FigureCanvas(window.figure4)
        heatmap_layout.addWidget(window.canvas4)

        window.updateHeatmapBtn = QtWidgets.QPushButton("Обновить карту")
        heatmap_layout.addWidget(window.updateHeatmapBtn)

        window.exportHeatmapBtn = QtWidgets.QPushButton("Экспорт карты")
        heatmap_layout.addWidget(window.exportHeatmapBtn)
        window.exportHeatmapBtn.clicked.connect(lambda: export_chart(window))  # ✅ ДОБАВЬ ЭТО

    def update_interaction():
        """Обновляет график взаимодействия"""
        if window.data is None:
            window.show_error_message("Нет данных для построения графика")
            return
        
        try:
            success = create_interaction_plot(window)
            if not success:
                window.show_error_message("Не удалось создать график взаимодействия")
        except Exception as e:
            window.show_error_message(f"Ошибка при создании графика взаимодействия: {str(e)}")

    def update_heatmap():
        """Обновляет тепловую карту"""
        if window.data is None:
            window.show_error_message("Нет данных для построения тепловой карты")
            return
        
        try:
            success = create_heatmap(window)
            if not success:
                window.show_error_message("Не удалось создать тепловую карту")
        except Exception as e:
            window.show_error_message(f"Ошибка при создании тепловой карты: {str(e)}")

    # Подключение обработчиков событий
    window.chartTypeCombo.currentTextChanged.connect(lambda: update_main_chart(window))
    window.showTrendCheck.stateChanged.connect(lambda: update_main_chart(window))
    window.exportChartBtn.clicked.connect(lambda: export_chart(window))
    window.radioButton.toggled.connect(lambda: update_comparison_chart(window))
    window.radioButton_2.toggled.connect(lambda: update_comparison_chart(window))
    
    # Подключение обработчиков для новых кнопок
    if hasattr(window, 'updateInteractionBtn'):
        window.updateInteractionBtn.clicked.connect(update_interaction)
    
    if hasattr(window, 'updateHeatmapBtn'):
        window.updateHeatmapBtn.clicked.connect(update_heatmap)