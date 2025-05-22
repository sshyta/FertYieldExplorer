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
    QVBoxLayout, QWidget)

import ui.res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1025, 685)
        MainWindow.setStyleSheet(u"background-color: #424242;\n"
"font: 600 9pt \"Noto Sans\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(40, 90, 951, 571))
        self.HomePage = QWidget()
        self.HomePage.setObjectName(u"HomePage")
        self.toolButton = QToolButton(self.HomePage)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(760, 40, 141, 181))
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/logo.webp", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(150, 150))
        self.layoutWidget = QWidget(self.HomePage)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 360, 520, 194))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_2.addWidget(self.textEdit)

        self.textEdit_2 = QTextEdit(self.layoutWidget)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.horizontalLayout_2.addWidget(self.textEdit_2)

        self.stackedWidget.addWidget(self.HomePage)
        self.DataPage = QWidget()
        self.DataPage.setObjectName(u"DataPage")
        self.DataTable = QTableView(self.DataPage)
        self.DataTable.setObjectName(u"DataTable")
        self.DataTable.setGeometry(QRect(10, 60, 921, 491))
        self.layoutWidget1 = QWidget(self.DataPage)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 436, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.LoadBtn = QPushButton(self.layoutWidget1)
        self.LoadBtn.setObjectName(u"LoadBtn")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/upload_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.LoadBtn.setIcon(icon1)
        self.LoadBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.LoadBtn)

        self.statusLabel = QLabel(self.layoutWidget1)
        self.statusLabel.setObjectName(u"statusLabel")

        self.horizontalLayout_3.addWidget(self.statusLabel)

        self.SaveBtn = QPushButton(self.layoutWidget1)
        self.SaveBtn.setObjectName(u"SaveBtn")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/download_done_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SaveBtn.setIcon(icon2)
        self.SaveBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.SaveBtn)

        self.ExportBtn = QPushButton(self.layoutWidget1)
        self.ExportBtn.setObjectName(u"ExportBtn")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/download_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ExportBtn.setIcon(icon3)
        self.ExportBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.ExportBtn)

        self.stackedWidget.addWidget(self.DataPage)
        self.AnalysisPage = QWidget()
        self.AnalysisPage.setObjectName(u"AnalysisPage")
        self.analysisGroupBox = QGroupBox(self.AnalysisPage)
        self.analysisGroupBox.setObjectName(u"analysisGroupBox")
        self.analysisGroupBox.setGeometry(QRect(30, 30, 361, 321))
        self.runAnalysisBtn = QPushButton(self.analysisGroupBox)
        self.runAnalysisBtn.setObjectName(u"runAnalysisBtn")
        self.runAnalysisBtn.setGeometry(QRect(30, 160, 149, 25))
        self.testTypeCombo = QComboBox(self.analysisGroupBox)
        self.testTypeCombo.addItem("")
        self.testTypeCombo.addItem("")
        self.testTypeCombo.setObjectName(u"testTypeCombo")
        self.testTypeCombo.setGeometry(QRect(190, 60, 149, 25))
        self.layoutWidget2 = QWidget(self.analysisGroupBox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 60, 151, 81))
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.cropFactorCheck = QCheckBox(self.layoutWidget2)
        self.cropFactorCheck.setObjectName(u"cropFactorCheck")

        self.verticalLayout.addWidget(self.cropFactorCheck)

        self.fertilizerCheck = QCheckBox(self.layoutWidget2)
        self.fertilizerCheck.setObjectName(u"fertilizerCheck")

        self.verticalLayout.addWidget(self.fertilizerCheck)

        self.interactionCheck = QCheckBox(self.layoutWidget2)
        self.interactionCheck.setObjectName(u"interactionCheck")

        self.verticalLayout.addWidget(self.interactionCheck)

        self.resultsText = QTextEdit(self.AnalysisPage)
        self.resultsText.setObjectName(u"resultsText")
        self.resultsText.setGeometry(QRect(400, 40, 521, 501))
        self.stackedWidget.addWidget(self.AnalysisPage)
        self.ChartsPage = QWidget()
        self.ChartsPage.setObjectName(u"ChartsPage")
        self.chartsTabs = QTabWidget(self.ChartsPage)
        self.chartsTabs.setObjectName(u"chartsTabs")
        self.chartsTabs.setGeometry(QRect(20, 50, 861, 481))
        self.mainChartTab = QWidget()
        self.mainChartTab.setObjectName(u"mainChartTab")
        self.verticalLayoutWidget = QWidget(self.mainChartTab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 201, 151))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.chartTypeCombo = QComboBox(self.verticalLayoutWidget)
        self.chartTypeCombo.addItem("")
        self.chartTypeCombo.addItem("")
        self.chartTypeCombo.addItem("")
        self.chartTypeCombo.setObjectName(u"chartTypeCombo")

        self.verticalLayout_4.addWidget(self.chartTypeCombo)

        self.showTrendCheck = QCheckBox(self.verticalLayoutWidget)
        self.showTrendCheck.setObjectName(u"showTrendCheck")

        self.verticalLayout_4.addWidget(self.showTrendCheck)

        self.exportChartBtn = QPushButton(self.verticalLayoutWidget)
        self.exportChartBtn.setObjectName(u"exportChartBtn")
        self.exportChartBtn.setIcon(icon3)
        self.exportChartBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.exportChartBtn)

        self.mainPlotContainer = QWidget(self.mainChartTab)
        self.mainPlotContainer.setObjectName(u"mainPlotContainer")
        self.mainPlotContainer.setGeometry(QRect(260, 20, 571, 421))
        self.chartsTabs.addTab(self.mainChartTab, "")
        self.comparisonTab = QWidget()
        self.comparisonTab.setObjectName(u"comparisonTab")
        self.groupBox = QGroupBox(self.comparisonTab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 191, 166))
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 60, 94, 21))
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(20, 90, 94, 21))
        self.comparisonPlotContainer = QWidget(self.comparisonTab)
        self.comparisonPlotContainer.setObjectName(u"comparisonPlotContainer")
        self.comparisonPlotContainer.setGeometry(QRect(260, 20, 571, 421))
        self.chartsTabs.addTab(self.comparisonTab, "")
        self.stackedWidget.addWidget(self.ChartsPage)
        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(40, 40, 345, 32))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.HomeBtn = QPushButton(self.layoutWidget3)
        self.HomeBtn.setObjectName(u"HomeBtn")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/home_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.HomeBtn.setIcon(icon4)
        self.HomeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.HomeBtn)

        self.dataBtn = QPushButton(self.layoutWidget3)
        self.dataBtn.setObjectName(u"dataBtn")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icons/database_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dataBtn.setIcon(icon5)
        self.dataBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.dataBtn)

        self.analysisBtn = QPushButton(self.layoutWidget3)
        self.analysisBtn.setObjectName(u"analysisBtn")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icons/experiment_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.analysisBtn.setIcon(icon6)
        self.analysisBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.analysisBtn)

        self.chartsBtn = QPushButton(self.layoutWidget3)
        self.chartsBtn.setObjectName(u"chartsBtn")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/icons/bar_chart_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.chartsBtn.setIcon(icon7)
        self.chartsBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.chartsBtn)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.chartsTabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toolButton.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f \u0443\u0440\u043e\u0436\u0430\u0439\u043d\u043e\u0441\u0442\u0438 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u0445 \u0441\u043e\u0440\u0442\u043e\u0432 \u0441\u0435\u043b\u044c\u0441\u043a\u043e\u0445\u043e\u0437\u044f\u0439\u0441"
                        "\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u043a\u0443\u043b\u044c\u0442\u0443\u0440 \u043f\u0440\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0438 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u0445 \u0442\u0438\u043f\u043e\u0432 \u0443\u0434\u043e\u0431\u0440\u0435\u043d\u0438\u0439</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u043b\u0438 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u044b \u0433\u0440\u0443\u043f\u043f\u044b \u0446\u0438\u0441-33<br />\u0421\u043c\u0438\u0440\u043d\u043e\u0432 \u041c.\u0410.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0411\u043b\u0438\u043d\u043e\u0432 \u0418.\u0410"
                        ".</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041b\u0435\u0448\u0438\u043d\u0430 \u0414.\u0410.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.LoadBtn.setText(QCoreApplication.translate("MainWindow", u"Load Data", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.SaveBtn.setText(QCoreApplication.translate("MainWindow", u"Save Data", None))
        self.ExportBtn.setText(QCoreApplication.translate("MainWindow", u"Export Results", None))
        self.analysisGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0430\u043d\u0430\u043b\u0438\u0437\u0430", None))
        self.runAnalysisBtn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0430\u043d\u0430\u043b\u0438\u0437", None))
        self.testTypeCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"ANOVA", None))
        self.testTypeCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Tukey HSD", None))

        self.cropFactorCheck.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442 \u043a\u0443\u043b\u044c\u0442\u0443\u0440\u044b", None))
        self.fertilizerCheck.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0443\u0434\u043e\u0431\u0440\u0435\u043d\u0438\u044f", None))
        self.interactionCheck.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.chartTypeCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"columnar", None))
        self.chartTypeCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Spot", None))
        self.chartTypeCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"linear", None))

        self.showTrendCheck.setText(QCoreApplication.translate("MainWindow", u"Show Trend", None))
        self.exportChartBtn.setText(QCoreApplication.translate("MainWindow", u"Export graph", None))
        self.chartsTabs.setTabText(self.chartsTabs.indexOf(self.mainChartTab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e \u0441\u043e\u0440\u0442\u0430\u043c", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e \u0443\u0434\u043e\u0431\u0440\u0435\u043d\u0438\u044f\u043c", None))
        self.chartsTabs.setTabText(self.chartsTabs.indexOf(self.comparisonTab), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.HomeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"data", None))
        self.analysisBtn.setText(QCoreApplication.translate("MainWindow", u"analysis", None))
        self.chartsBtn.setText(QCoreApplication.translate("MainWindow", u"charts", None))
    # retranslateUi

