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

        # Кнопка "Создать тестовые данные" с улучшенным стилем
        self.SampleDataBtn = QPushButton("Создать тестовые данные", self.DataPage)
        self.SampleDataBtn.setMinimumSize(QSize(220, 40))
        self.SampleDataBtn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #e67e22, stop:1 #d35400);
                border: 2px solid #d35400;
                border-radius: 8px;
                color: white;
                font-size: 14pt;
                font-weight: 600;
                padding: 12px 20px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #f39c12, stop:1 #e67e22);
                border: 2px solid #e67e22;
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #d35400, stop:1 #a04000);
            }
        """)

        # Добавляем кнопку в layout
        self.horizontalLayout_3.insertWidget(1, self.SampleDataBtn)
        
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/upload_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.SampleDataBtn.setIcon(icon1)
        self.SampleDataBtn.setIconSize(QSize(24, 24))
        
        # Обновление заголовков вкладок
        self.chartsTabs.setTabText(0, "Основной график")
        self.chartsTabs.setTabText(1, "График сравнения")
        
    def show_error_message(self, text):
        """Отображает сообщение об ошибке с улучшенным стилем"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Ошибка")
        msg.setText(text)
        msg.setStyleSheet("""
    QMessageBox {
        background-color: #ecf0f1;
        color: #2c3e50;
        font-size: 12pt;
    }
    QMessageBox QLabel {
        color: #2c3e50;
        font-size: 12pt;
        font-weight: 500;
    }
    QMessageBox QPushButton {
        background: #e74c3c;
        border: 2px solid #c0392b;
        border-radius: 6px;
        color: white;
        font-size: 11pt;
        font-weight: 600;
        padding: 8px 16px;
        min-width: 80px;
    }
    QMessageBox QPushButton:hover {
        background: #ec7063;
    }
""")
        msg.exec()

    def show_info_message(self, text):
        """Отображает информационное сообщение с улучшенным стилем"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Информация")
        msg.setText(text)
        msg.setStyleSheet("""
    QMessageBox {
        background-color: #ecf0f1;
        color: #2c3e50;
        font-size: 12pt;
    }
    QMessageBox QLabel {
        color: #2c3e50;
        font-size: 12pt;
        font-weight: 500;
    }
    QMessageBox QPushButton {
        background: #3498db;
        border: 2px solid #2980b9;
        border-radius: 6px;
        color: white;
        font-size: 11pt;
        font-weight: 600;
        padding: 8px 16px;
        min-width: 80px;
    }
    QMessageBox QPushButton:hover {
        background: #5dade2;
    }
""")
        msg.exec()
