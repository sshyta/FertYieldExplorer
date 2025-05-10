from PyQt6.QtWidgets import QMainWindow
from ui.ui_main import Ui_MainWindow
from views.data_view import setup_data_page
from views.analysis_view import setup_analysis_page
from views.charts_view import setup_charts_page

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Хранилище данных
        self.data = None

        # Настройка вкладок
        setup_data_page(self)
        setup_analysis_page(self)
        setup_charts_page(self)

        # Навигация
        self.HomeBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.dataBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.analysisBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.chartsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

    def show_error_message(self, text):
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.critical(self, "Ошибка", text)