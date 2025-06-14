# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
                             QHBoxLayout, QHeaderView, QLabel, QMainWindow,
                             QPushButton, QRadioButton, QSizePolicy, QStackedWidget,
                             QTabWidget, QTableView, QTextEdit, QToolButton,
                             QVBoxLayout, QWidget, QSpacerItem)

import ui.res_rc

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        # Увеличиваем размер окна для лучшей презентации
        MainWindow.resize(1400, 900)
        
        # Современная цветовая схема и улучшенные стили
        MainWindow.setStyleSheet(u"""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2c3e50, stop:1 #34495e);
                color: #ecf0f1;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-size: 11pt;
                font-weight: 500;
            }
            
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #3498db, stop:1 #2980b9);
                border: 2px solid #2980b9;
                border-radius: 8px;
                color: white;
                font-size: 14pt;
                font-weight: 600;
                padding: 12px 20px;
                min-height: 20px;
            }
            
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #5dade2, stop:1 #3498db);
                border: 2px solid #3498db;
            }
            
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2980b9, stop:1 #1f618d);
            }
            
            QGroupBox {
                background: rgba(52, 73, 94, 0.8);
                border: 2px solid #34495e;
                border-radius: 10px;
                font-size: 14pt;
                font-weight: 600;
                color: #ecf0f1;
                padding-top: 20px;
                margin-top: 10px;
            }
            
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 5px 10px;
                background: #3498db;
                border-radius: 5px;
                color: white;
            }
            
            QComboBox {
                background: #ecf0f1;
                border: 2px solid #bdc3c7;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 12pt;
                color: #2c3e50;
                min-height: 20px;
                selection-background-color: white;
            }

            QComboBox:hover {
                border: 2px solid #3498db;
            }

            QComboBox::drop-down {
                border: none;
                width: 30px;
                background: transparent;
            }

            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 8px solid #2c3e50;
                margin-right: 10px;
            }

            QComboBox QAbstractItemView {
                background: white;
                border: 2px solid #bdc3c7;
                border-radius: 6px;
                selection-background-color: #e8f4fd;
                selection-color: #2c3e50;
                color: #2c3e50;
                font-size: 12pt;
                padding: 4px;
            }

            QComboBox QAbstractItemView::item {
                background: white;
                color: #2c3e50;
                padding: 8px 12px;
                border: none;
                min-height: 20px;
            }

            QComboBox QAbstractItemView::item:selected {
                background: #e8f4fd;
                color: #2c3e50;
            }

            QComboBox QAbstractItemView::item:hover {
                background: #d6eaf8;
                color: #2c3e50;
            }
            
            QCheckBox {
                font-size: 12pt;
                color: #ecf0f1;
                spacing: 8px;
            }
            
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #bdc3c7;
                border-radius: 4px;
                background: #ecf0f1;
            }
            
            QCheckBox::indicator:checked {
                background: #3498db;
                border: 2px solid #2980b9;
            }
            
            QRadioButton {
                font-size: 12pt;
                color: #ecf0f1;
                spacing: 8px;
            }
            
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #bdc3c7;
                border-radius: 9px;
                background: #ecf0f1;
            }
            
            QRadioButton::indicator:checked {
                background: #3498db;
                border: 2px solid #2980b9;
            }
            
            QLabel {
                color: #ecf0f1;
                font-size: 12pt;
                font-weight: 500;
            }
            
            QTextEdit {
                background: rgba(236, 240, 241, 0.95);
                border: 2px solid #bdc3c7;
                border-radius: 8px;
                padding: 10px;
                font-size: 11pt;
                color: #2c3e50;
            }
            
            QTableView {
                background: #ecf0f1;
                border: 2px solid #bdc3c7;
                border-radius: 8px;
                gridline-color: #bdc3c7;
                font-size: 11pt;
                color: #2c3e50;
            }
            
            QTableView::item {
                padding: 8px;
                border-bottom: 1px solid #bdc3c7;
            }
            
            QTableView::item:selected {
                background: #3498db;
                color: white;
            }
            
            QTabWidget::pane {
                border: 2px solid #34495e;
                border-radius: 8px;
                background: rgba(52, 73, 94, 0.8);
            }
            
            QTabBar::tab {
                background: #34495e;
                color: #ecf0f1;
                padding: 12px 20px;
                margin-right: 2px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                font-size: 14pt;
                font-weight: 500;
                min-width: 200px;
                height: 20px;
            }
            
            QTabBar::tab:selected {
                background: #3498db;
                color: white;
            }
            
            QTabBar::tab:hover {
                background: #5dade2;
            }
        """)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        # Увеличиваем размеры основного контейнера
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(50, 120, 1300, 750))
        
        # Главная страница
        self.HomePage = QWidget()
        self.HomePage.setObjectName(u"HomePage")
        
        # Логотип (увеличиваем размер и делаем фон прозрачным)
        self.toolButton = QToolButton(self.HomePage)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(1000, 50, 200, 240))
        self.toolButton.setStyleSheet("""
    QToolButton {
        background: transparent;
        border: none;
        border-radius: 10px;
    }
    QToolButton:hover {
        background: rgba(52, 73, 94, 0.3);
        border-radius: 10px;
    }
""")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/logo.webp", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(200, 200))
        
        # Заголовок приложения - сверху (увеличиваем размеры)
        self.textEdit = QTextEdit(self.HomePage)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(50, 50, 900, 220))
        
        # Информация об авторах - снизу (увеличиваем размеры)
        self.textEdit_2 = QTextEdit(self.HomePage)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(50, 500, 700, 200))

        self.stackedWidget.addWidget(self.HomePage)
        
        # Страница данных
        self.DataPage = QWidget()
        self.DataPage.setObjectName(u"DataPage")
        
        # Увеличиваем таблицу данных
        self.DataTable = QTableView(self.DataPage)
        self.DataTable.setObjectName(u"DataTable")
        self.DataTable.setGeometry(QRect(20, 80, 1260, 650))
        
        # Контейнер для кнопок (увеличиваем размеры)
        self.layoutWidget1 = QWidget(self.DataPage)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 20, 1260, 60))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(15)
        
        # Увеличиваем кнопки
        self.LoadBtn = QPushButton(self.layoutWidget1)
        self.LoadBtn.setMinimumSize(QSize(180, 40))
        self.LoadBtn.setObjectName(u"LoadBtn")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/upload_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.LoadBtn.setIcon(icon1)
        self.LoadBtn.setIconSize(QSize(24, 24))
        self.horizontalLayout_3.addWidget(self.LoadBtn)

        self.statusLabel = QLabel(self.layoutWidget1)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setStyleSheet("font-size: 14pt; font-weight: 600;")
        self.horizontalLayout_3.addWidget(self.statusLabel)

        self.SaveBtn = QPushButton(self.layoutWidget1)
        self.SaveBtn.setMinimumSize(QSize(180, 40))
        self.SaveBtn.setObjectName(u"SaveBtn")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/download_done_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SaveBtn.setIcon(icon2)
        self.SaveBtn.setIconSize(QSize(24, 24))
        self.horizontalLayout_3.addWidget(self.SaveBtn)

        self.ExportBtn = QPushButton(self.layoutWidget1)
        self.ExportBtn.setMinimumSize(QSize(200, 40))
        self.ExportBtn.setObjectName(u"ExportBtn")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/download_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ExportBtn.setIcon(icon3)
        self.ExportBtn.setIconSize(QSize(24, 24))
        self.horizontalLayout_3.addWidget(self.ExportBtn)

        self.stackedWidget.addWidget(self.DataPage)
        
        # Страница анализа
        self.AnalysisPage = QWidget()
        self.AnalysisPage.setObjectName(u"AnalysisPage")
        
        # Увеличиваем группу параметров анализа
        self.analysisGroupBox = QGroupBox(self.AnalysisPage)
        self.analysisGroupBox.setObjectName(u"analysisGroupBox")
        self.analysisGroupBox.setGeometry(QRect(40, 40, 480, 420))
        
        # Увеличиваем кнопку запуска анализа
        self.runAnalysisBtn = QPushButton(self.analysisGroupBox)
        self.runAnalysisBtn.setObjectName(u"runAnalysisBtn")
        self.runAnalysisBtn.setGeometry(QRect(40, 200, 200, 45))
        
        # Увеличиваем выпадающий список
        self.testTypeCombo = QComboBox(self.analysisGroupBox)
        self.testTypeCombo.addItem("")
        self.testTypeCombo.addItem("")
        self.testTypeCombo.setObjectName(u"testTypeCombo")
        self.testTypeCombo.setGeometry(QRect(250, 80, 200, 35))
        
        # Контейнер для чекбоксов
        self.layoutWidget2 = QWidget(self.analysisGroupBox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(40, 80, 200, 100))
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        
        self.cropFactorCheck = QCheckBox(self.layoutWidget2)
        self.cropFactorCheck.setObjectName(u"cropFactorCheck")
        self.verticalLayout.addWidget(self.cropFactorCheck)

        self.fertilizerCheck = QCheckBox(self.layoutWidget2)
        self.fertilizerCheck.setObjectName(u"fertilizerCheck")
        self.verticalLayout.addWidget(self.fertilizerCheck)

        self.interactionCheck = QCheckBox(self.layoutWidget2)
        self.interactionCheck.setObjectName(u"interactionCheck")
        self.verticalLayout.addWidget(self.interactionCheck)

        # Увеличиваем область результатов
        self.resultsText = QTextEdit(self.AnalysisPage)
        self.resultsText.setObjectName(u"resultsText")
        self.resultsText.setGeometry(QRect(550, 40, 710, 680))
        
        self.stackedWidget.addWidget(self.AnalysisPage)
        
        # Страница графиков
        self.ChartsPage = QWidget()
        self.ChartsPage.setObjectName(u"ChartsPage")
        
        # Увеличиваем вкладки графиков
        self.chartsTabs = QTabWidget(self.ChartsPage)
        self.chartsTabs.setObjectName(u"chartsTabs")
        self.chartsTabs.setGeometry(QRect(30, 60, 1240, 660))
        
        # Основной график
        self.mainChartTab = QWidget()
        self.mainChartTab.setObjectName(u"mainChartTab")
        
        # Контейнер для настроек графика
        self.verticalLayoutWidget = QWidget(self.mainChartTab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 30, 280, 200))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(15)
        
        # Увеличиваем элементы управления
        self.chartTypeCombo = QComboBox(self.verticalLayoutWidget)
        self.chartTypeCombo.addItem("")
        self.chartTypeCombo.addItem("")
        self.chartTypeCombo.setObjectName(u"chartTypeCombo")
        self.chartTypeCombo.setMinimumHeight(35)
        self.verticalLayout_4.addWidget(self.chartTypeCombo)

        self.showTrendCheck = QCheckBox(self.verticalLayoutWidget)
        self.showTrendCheck.setObjectName(u"showTrendCheck")
        self.verticalLayout_4.addWidget(self.showTrendCheck)

        self.exportChartBtn = QPushButton(self.verticalLayoutWidget)
        self.exportChartBtn.setObjectName(u"exportChartBtn")
        self.exportChartBtn.setIcon(icon3)
        self.exportChartBtn.setIconSize(QSize(24, 24))
        self.exportChartBtn.setMinimumHeight(40)
        self.verticalLayout_4.addWidget(self.exportChartBtn)

        # Увеличиваем контейнер для графика
        self.mainPlotContainer = QWidget(self.mainChartTab)
        self.mainPlotContainer.setObjectName(u"mainPlotContainer")
        self.mainPlotContainer.setGeometry(QRect(340, 30, 860, 580))
        
        self.chartsTabs.addTab(self.mainChartTab, "")
        
        # График сравнения
        self.comparisonTab = QWidget()
        self.comparisonTab.setObjectName(u"comparisonTab")
        # Кнопка экспорта графика сравнения
        self.exportComparisonChartBtn = QPushButton(self.comparisonTab)
        self.exportComparisonChartBtn.setObjectName(u"exportComparisonChartBtn")
        self.exportComparisonChartBtn.setText("Экспорт графика")
        self.exportComparisonChartBtn.setIcon(icon3)
        self.exportComparisonChartBtn.setIconSize(QSize(24, 24))
        self.exportComparisonChartBtn.setMinimumHeight(40)
        self.exportComparisonChartBtn.setGeometry(QRect(30, 270, 280, 40))  # Под groupBox (220px высота + 10px отступ)

        
        # Увеличиваем группу настроек
        self.groupBox = QGroupBox(self.comparisonTab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 30, 280, 220))
        
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(30, 80, 200, 30))
        
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(30, 120, 200, 30))
        
        # Увеличиваем контейнер для графика сравнения
        self.comparisonPlotContainer = QWidget(self.comparisonTab)
        self.comparisonPlotContainer.setObjectName(u"comparisonPlotContainer")
        self.comparisonPlotContainer.setGeometry(QRect(340, 30, 860, 580))
        
        self.chartsTabs.addTab(self.comparisonTab, "")
        self.stackedWidget.addWidget(self.ChartsPage)
        
        # Навигационные кнопки (увеличиваем размеры)
        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(50, 50, 1300, 60))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(25)
        
        # Увеличиваем навигационные кнопки
        self.HomeBtn = QPushButton(self.layoutWidget3)
        self.HomeBtn.setMinimumSize(QSize(200, 50))
        self.HomeBtn.setObjectName(u"HomeBtn")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/home_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.HomeBtn.setIcon(icon4)
        self.HomeBtn.setIconSize(QSize(28, 28))
        self.horizontalLayout.addWidget(self.HomeBtn)

        self.dataBtn = QPushButton(self.layoutWidget3)
        self.dataBtn.setMinimumSize(QSize(200, 50))
        self.dataBtn.setObjectName(u"dataBtn")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icons/database_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dataBtn.setIcon(icon5)
        self.dataBtn.setIconSize(QSize(28, 28))
        self.horizontalLayout.addWidget(self.dataBtn)

        self.analysisBtn = QPushButton(self.layoutWidget3)
        self.analysisBtn.setMinimumSize(QSize(200, 50))
        self.analysisBtn.setObjectName(u"analysisBtn")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icons/experiment_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.analysisBtn.setIcon(icon6)
        self.analysisBtn.setIconSize(QSize(28, 28))
        self.horizontalLayout.addWidget(self.analysisBtn)

        self.chartsBtn = QPushButton(self.layoutWidget3)
        self.chartsBtn.setMinimumSize(QSize(200, 50))
        self.chartsBtn.setObjectName(u"chartsBtn")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/icons/bar_chart_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.chartsBtn.setIcon(icon7)
        self.chartsBtn.setIconSize(QSize(28, 28))
        self.horizontalLayout.addWidget(self.chartsBtn)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.chartsTabs.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Анализ урожайности сельскохозяйственных культур", None))
        self.toolButton.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:500; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:700; color:#2c3e50;\">\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f \u0443\u0440\u043e\u0436\u0430\u0439\u043d\u043e\u0441\u0442\u0438 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u0445 \u0441\u043e\u0440\u0442\u043e\u0432 \u0441\u0435\u043b\u044c\u0441\u043a\u043e\u0445\u043e\u0437\u044f\u0439\u0441"
                        "\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u043a\u0443\u043b\u044c\u0442\u0443\u0440 \u043f\u0440\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0438 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u0445 \u0442\u0438\u043f\u043e\u0432 \u0443\u0434\u043e\u0431\u0440\u0435\u043d\u0438\u0439</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:500; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#2c3e50;\">\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u043b\u0438 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u044b \u0433\u0440\u0443\u043f\u043f\u044b \u0446\u0438\u0441-33</span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#34495e;\">\u0421\u043c\u0438\u0440\u043d\u043e\u0432 \u041c.\u0410.</span></p>\n"
"<p style=\" margin-top:5px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#34495e;\">\u0411\u043b\u0438\u043d\u043e\u0432 \u0418.\u0410.</span></p>\n"
"<p style=\" margin-top:5px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#34495e;\">\u041b\u0435\u0448\u0438\u043d\u0430 \u0414.\u0410.</span></p></body></html>", None))
        self.LoadBtn.setText(QCoreApplication.translate("MainWindow", u"Загрузка данных", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Файл не выбран", None))
        self.SaveBtn.setText(QCoreApplication.translate("MainWindow", u"Сохранение данных", None))
        self.ExportBtn.setText(QCoreApplication.translate("MainWindow", u"Выгрузить результаты (полный отчет)", None))
        self.analysisGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Параметры анализа", None))
        self.runAnalysisBtn.setText(QCoreApplication.translate("MainWindow", u"Запустить анализ", None))
        self.testTypeCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"ANOVA", None))
        self.testTypeCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Tukey HSD", None))
        self.cropFactorCheck.setText(QCoreApplication.translate("MainWindow", u"Сорт культуры", None))
        self.fertilizerCheck.setText(QCoreApplication.translate("MainWindow", u"Тип удобрения", None))
        self.interactionCheck.setText(QCoreApplication.translate("MainWindow", u"Взаимодействие", None))
        self.chartTypeCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Столбчатая диаграмма", None))
        self.chartTypeCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Точечная диаграмма", None))
        self.showTrendCheck.setText(QCoreApplication.translate("MainWindow", u"Показать тренд", None))
        self.exportChartBtn.setText(QCoreApplication.translate("MainWindow", u"Экспортировать график", None))
        self.chartsTabs.setTabText(self.chartsTabs.indexOf(self.mainChartTab), QCoreApplication.translate("MainWindow", u"Основной график", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Группировка", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"по сортам", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"по удобрениям", None))
        self.chartsTabs.setTabText(self.chartsTabs.indexOf(self.comparisonTab), QCoreApplication.translate("MainWindow", u"График сравнения", None))
        self.HomeBtn.setText(QCoreApplication.translate("MainWindow", u"Главная страница", None))
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"Данные", None))
        self.analysisBtn.setText(QCoreApplication.translate("MainWindow", u"Анализ", None))
        self.chartsBtn.setText(QCoreApplication.translate("MainWindow", u"Графики", None))

        # Тексты для дополнительных кнопок (если они существуют)
        if hasattr(self, 'updateInteractionBtn'):
            self.updateInteractionBtn.setText("Построить график взаимодействия")
        if hasattr(self, 'updateHeatmapBtn'):
            self.updateHeatmapBtn.setText("Обновить тепловую карту")
    # retranslateUi