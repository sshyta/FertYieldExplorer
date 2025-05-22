from PyQt6 import QtWidgets
from PyQt6.QtCore import QRect  # Добавлен правильный импорт QRect
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
    layout2 = window.comparisonPlotContainer.layout() or QtWidgets.QVBoxLayout(window.comparisonPlotContainer)
    layout2.addWidget(window.canvas2)

    # Обновление списка типов графиков
    window.chartTypeCombo.clear()
    window.chartTypeCombo.addItems(["Столбчатая", "Ящик с усами", "Точечная"])

    # Добавление новых вкладок для дополнительных графиков
    if window.chartsTabs.count() == 2:  # Если есть только две стандартные вкладки
        # Добавление вкладки для графика взаимодействия
        interaction_tab = QtWidgets.QWidget()
        window.chartsTabs.addTab(interaction_tab, "Взаимодействие")
        
        # Контейнер для графика взаимодействия
        window.interactionPlotContainer = QtWidgets.QWidget(interaction_tab)
        window.interactionPlotContainer.setGeometry(QRect(20, 20, 800, 400))  # Исправлено: используем QRect из QtCore
        
        # Настройка графика взаимодействия
        window.figure3 = Figure(figsize=(8, 4), dpi=100)
        window.canvas3 = FigureCanvas(window.figure3)
        layout3 = QtWidgets.QVBoxLayout(window.interactionPlotContainer)
        layout3.addWidget(window.canvas3)
        
        # Кнопка для обновления графика взаимодействия
        window.updateInteractionBtn = QtWidgets.QPushButton("Обновить график", interaction_tab)
        window.updateInteractionBtn.setGeometry(QRect(20, 430, 150, 30))  # Исправлено: используем QRect из QtCore
        
        # Добавление вкладки для тепловой карты
        heatmap_tab = QtWidgets.QWidget()
        window.chartsTabs.addTab(heatmap_tab, "Тепловая карта")
        
        # Контейнер для тепловой карты
        window.heatmapContainer = QtWidgets.QWidget(heatmap_tab)
        window.heatmapContainer.setGeometry(QRect(20, 20, 800, 400))  # Исправлено: используем QRect из QtCore
        
        # Настройка тепловой карты
        window.figure4 = Figure(figsize=(8, 4), dpi=100)
        window.canvas4 = FigureCanvas(window.figure4)
        layout4 = QtWidgets.QVBoxLayout(window.heatmapContainer)
        layout4.addWidget(window.canvas4)
        
        # Кнопка для обновления тепловой карты
        window.updateHeatmapBtn = QtWidgets.QPushButton("Обновить карту", heatmap_tab)
        window.updateHeatmapBtn.setGeometry(QRect(20, 430, 150, 30))  # Исправлено: используем QRect из QtCore

    def update_interaction():
        """Обновляет график взаимодействия"""
        if window.data is None:
            window.show_error_message("Нет данных для построения графика")
            return
        
        try:
            # Создание графика взаимодействия
            window.figure3.clear()
            interaction_fig = create_interaction_plot(window.data)
            
            if interaction_fig:
                # Копирование графика на canvas
                for ax in interaction_fig.get_axes():
                    window.figure3.add_axes(ax)
                window.canvas3.draw()
            else:
                window.show_error_message("Не удалось создать график взаимодействия")
        except Exception as e:
            window.show_error_message(f"Ошибка при создании графика взаимодействия: {str(e)}")

    def update_heatmap():
        """Обновляет тепловую карту"""
        if window.data is None:
            window.show_error_message("Нет данных для построения тепловой карты")
            return
        
        try:
            # Создание тепловой карты
            window.figure4.clear()
            heatmap_fig = create_heatmap(window.data)
            
            if heatmap_fig:
                # Копирование графика на canvas
                for ax in heatmap_fig.get_axes():
                    window.figure4.add_axes(ax)
                window.canvas4.draw()
            else:
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