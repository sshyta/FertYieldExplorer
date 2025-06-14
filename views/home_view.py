from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget
from ui.ui_main import Ui_MainWindow
from views.data_view import setup_data_page
from views.analysis_view import setup_analysis_page
from views.charts_view import setup_charts_page

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Анализ урожайности сельскохозяйственных культур")

        # Хранилище данных
        self.data = None

        # Добавление дополнительных элементов интерфейса
        self._add_ui_elements()

        # Настройка вкладок
        setup_data_page(self)
        setup_analysis_page(self)
        setup_charts_page(self)

        # Навигация
        self.HomeBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.dataBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.analysisBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.chartsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

    def _add_ui_elements(self):
        """Добавляет дополнительные элементы интерфейса"""

        # Кнопка "Создать тестовые данные" добавляется в layout с другими
        self.SampleDataBtn = QPushButton("Создать тестовые данные", self.DataPage)
        self.SampleDataBtn.setMinimumSize(QSize(100, 20))
        self.SampleDataBtn.setStyleSheet("font-size: 12pt;")

        # Добавляем кнопку в тот же horizontalLayout_3, где Load, Save, Export
        self.horizontalLayout_3.insertWidget(2, self.SampleDataBtn)  # Вставим в начало
        # Или в конец: self.horizontalLayout_3.addWidget(self.SampleDataBtn)
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/upload_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.SampleDataBtn.setIcon(icon1)
        self.SampleDataBtn.setIconSize(QSize(20, 20))
        # Обновление заголовков вкладок
        self.chartsTabs.setTabText(0, "Основной график")
        self.chartsTabs.setTabText(1, "График сравнения")
    def show_error_message(self, text):
        """Отображает сообщение об ошибке"""
        QMessageBox.critical(self, "Ошибка", text)

    def show_info_message(self, text):
        """Отображает информационное сообщение"""
        QMessageBox.information(self, "Информация", text)