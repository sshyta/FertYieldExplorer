import sys
import pandas as pd
import numpy as np
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from ui.ui_main import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Инициализация данных
        self.data = None
        self.current_plot_style = 'seaborn'
        
        # Настройка интерфейса
        self.setup_charts()
        self.translate_ui()
        self.setup_connections()
        
        # Пример тестовых данных (удалите в рабочей версии)
        self.load_test_data()
        
    def setup_charts(self):
        # Основной график
        self.figure1 = Figure(figsize=(5, 4), dpi=100)
        self.canvas1 = FigureCanvas(self.figure1)
        layout = QtWidgets.QVBoxLayout(self.mainPlotContainer)
        layout.addWidget(self.canvas1)
        
        # График сравнения
        self.figure2 = Figure(figsize=(5, 4), dpi=100)
        self.canvas2 = FigureCanvas(self.figure2)
        layout = QtWidgets.QVBoxLayout(self.comparisonPlotContainer)
        layout.addWidget(self.canvas2)
        
        # Настройка стилей
        self.set_plot_style(self.current_plot_style)
        
    def translate_ui(self):
        self.chartsTabs.setTabText(0, "Основные графики")
        self.chartsTabs.setTabText(1, "Сравнительный анализ")
        
        self.chartTypeCombo.clear()
        self.chartTypeCombo.addItems(["Столбчатая", "Линейная", "Ящик с усами", "Точечная"])
        
        self.showTrendCheck.setText("Показать тренд")
        self.exportChartBtn.setText("Экспорт графика")
        
        self.radioButton.setText("Группировать по сортам")
        self.radioButton_2.setText("Группировать по удобрениям")
        self.groupBox.setTitle("Тип группировки")
        
    def setup_connections(self):
        # Кнопки графиков
        self.chartTypeCombo.currentTextChanged.connect(self.update_main_chart)
        self.showTrendCheck.stateChanged.connect(self.update_main_chart)
        self.exportChartBtn.clicked.connect(self.export_chart)
        self.radioButton.toggled.connect(self.update_comparison_chart)
        self.radioButton_2.toggled.connect(self.update_comparison_chart)
        
        # Навигация
        self.HomeBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.dataBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.analysisBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.chartsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        
    def set_plot_style(self, style_name):
        plt.style.use('ggplot') 
        self.figure1.set_facecolor('#f0f0f0')
        self.figure2.set_facecolor('#f0f0f0')
        self.current_plot_style = style_name
        
    def load_test_data(self):
        data = {
            'Сорт': ['Пшеница']*4 + ['Ячмень']*4 + ['Рожь']*4,
            'Удобрение': ['Азотное', 'Фосфорное', 'Калийное', 'Комплексное']*3,
            'Урожайность': [25, 28, 23, 30, 22, 25, 20, 28, 20, 23, 18, 25]
        }
        self.data = pd.DataFrame(data)
        self.update_main_chart()
        self.update_comparison_chart()
        
    def update_main_chart(self):
        if self.data is None:
            return
            
        self.figure1.clear()
        ax = self.figure1.add_subplot(111)
        chart_type = self.chartTypeCombo.currentText()
        
        try:
            if chart_type == "Столбчатая":
                # Средняя урожайность по сортам
                avg_data = self.data.groupby('Сорт')['Урожайность'].mean()
                ax.bar(avg_data.index, avg_data.values, color='skyblue')
                ax.set_title('Средняя урожайность по сортам')
                ax.set_ylabel('Урожайность (ц/га)')
                
            elif chart_type == "Ящик с усами":
                # Распределение урожайности по удобрениям
                data_to_plot = [self.data[self.data['Удобрение'] == f]['Урожайность'] 
                              for f in self.data['Удобрение'].unique()]
                ax.boxplot(data_to_plot, labels=self.data['Удобрение'].unique())
                ax.set_title('Распределение урожайности по удобрениям')
                ax.set_ylabel('Урожайность (ц/га)')
                
            elif chart_type == "Точечная":
                # Зависимость урожайности от типа удобрения
                for crop in self.data['Сорт'].unique():
                    subset = self.data[self.data['Сорт'] == crop]
                    ax.scatter(subset['Удобрение'], subset['Урожайность'], label=crop)
                ax.legend()
                ax.set_title('Урожайность по сортам и удобрениям')
                ax.set_ylabel('Урожайность (ц/га)')
                
            if self.showTrendCheck.isChecked():
                # Линия среднего значения
                mean_yield = self.data['Урожайность'].mean()
                ax.axhline(mean_yield, color='r', linestyle='--', label='Среднее')
                ax.legend()
                
            self.canvas1.draw()
            
        except Exception as e:
            self.show_error_message(f"Ошибка построения графика: {str(e)}")
            
    def update_comparison_chart(self):
        if self.data is None:
            return
            
        self.figure2.clear()
        ax = self.figure2.add_subplot(111)
        
        try:
            if self.radioButton.isChecked():  # По сортам
                pivot_data = self.data.pivot_table(index='Удобрение', columns='Сорт', values='Урожайность')
                pivot_data.plot(kind='bar', ax=ax)
                ax.set_title('Сравнение урожайности по сортам')
            else:  # По удобрениям
                pivot_data = self.data.pivot_table(index='Сорт', columns='Удобрение', values='Урожайность')
                pivot_data.plot(kind='bar', ax=ax)
                ax.set_title('Сравнение урожайности по удобрениям')
                
            ax.set_ylabel('Урожайность (ц/га)')
            ax.legend(title='Легенда')
            self.canvas2.draw()
            
        except Exception as e:
            self.show_error_message(f"Ошибка сравнения: {str(e)}")
            
    def export_chart(self):
        if self.chartsTabs.currentIndex() == 0:
            figure = self.figure1
            default_name = "main_chart"
        else:
            figure = self.figure2
            default_name = "comparison_chart"
            
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Экспорт графика", default_name,
            "PNG (*.png);;PDF (*.pdf);;SVG (*.svg)")
            
        if file_path:
            try:
                figure.savefig(file_path, dpi=300, bbox_inches='tight')
                self.statusLabel.setText(f"График сохранен: {file_path}")
            except Exception as e:
                self.show_error_message(f"Ошибка экспорта: {str(e)}")
                
    def show_error_message(self, text):
        QMessageBox.critical(self, "Ошибка", text)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())