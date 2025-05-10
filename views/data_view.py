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
                window.DataTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
                window.statusLabel.setText(f"Файл загружен: {file_path}")
            except Exception as e:
                window.show_error_message(f"Ошибка загрузки: {str(e)}")

    window.LoadBtn.clicked.connect(load_data)