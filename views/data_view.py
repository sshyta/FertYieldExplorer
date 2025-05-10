import pandas as pd
from PyQt6.QtWidgets import QFileDialog, QAbstractItemView
from PyQt6.QtGui import QStandardItemModel, QStandardItem

def setup_data_page(window):
    def load_data():
        file_path, _ = QFileDialog.getOpenFileName(window, "Открыть CSV", "", "CSV Files (*.csv)")
        if file_path:
            try:
                window.data = pd.read_csv(file_path)
                model = QStandardItemModel()
                model.setHorizontalHeaderLabels(window.data.columns.tolist())
                for row in window.data.itertuples(index=False):
                    items = [QStandardItem(str(field)) for field in row]
                    model.appendRow(items)
                window.DataTable.setModel(model)
                window.statusLabel.setText(f"Файл загружен: {file_path}")
            except Exception as e:
                window.show_error_message(f"Ошибка загрузки: {str(e)}")

    def save_data():
        model = window.DataTable.model()
        if model is None:
            window.show_error_message("Нет данных для сохранения.")
            return

        rows = model.rowCount()
        cols = model.columnCount()
        data = []

        for row in range(rows):
            record = []
            for col in range(cols):
                item = model.item(row, col)
                record.append(item.text() if item else "")
            data.append(record)

        columns = [model.horizontalHeaderItem(i).text() for i in range(cols)]
        window.data = pd.DataFrame(data, columns=columns)
        window.statusLabel.setText("Данные обновлены в памяти.")

    def export_data():
        if window.data is None:
            window.show_error_message("Нет данных для экспорта.")
            return

        file_path, _ = QFileDialog.getSaveFileName(window, "Сохранить как CSV", "", "CSV Files (*.csv)")
        if file_path:
            try:
                window.data.to_csv(file_path, index=False)
                window.statusLabel.setText(f"Файл сохранён: {file_path}")
            except Exception as e:
                window.show_error_message(f"Ошибка при сохранении: {str(e)}")

    window.LoadBtn.clicked.connect(load_data)
    window.SaveBtn.clicked.connect(save_data)
    window.ExportBtn.clicked.connect(export_data)