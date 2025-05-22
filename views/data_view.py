import pandas as pd
from PyQt6.QtWidgets import QFileDialog, QAbstractItemView, QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import numpy as np

def setup_data_page(window):
    """
    Настраивает страницу работы с данными.
    
    Args:
        window: Главное окно приложения
    """
    def load_data():
        """Загружает данные из CSV-файла"""
        file_path, _ = QFileDialog.getOpenFileName(
            window, 
            "Открыть CSV", 
            "", 
            "CSV Files (*.csv);;Excel Files (*.xlsx *.xls);;All Files (*.*)"
        )
        
        if not file_path:
            return
        
        try:
            # Определение типа файла по расширению
            if file_path.lower().endswith(('.xlsx', '.xls')):
                window.data = pd.read_excel(file_path)
            else:
                # Для CSV пробуем разные разделители
                try:
                    window.data = pd.read_csv(file_path, sep=',')
                except:
                    try:
                        window.data = pd.read_csv(file_path, sep=';')
                    except:
                        window.data = pd.read_csv(file_path, sep='\t')
            
            # Проверка наличия необходимых колонок
            required_columns = ['Сорт', 'Удобрение', 'Урожайность']
            missing_columns = [col for col in required_columns if col not in window.data.columns]
            
            if missing_columns:
                # Если отсутствуют нужные колонки, пробуем переименовать существующие
                if len(window.data.columns) >= 3:
                    # Предполагаем, что первые три колонки содержат нужные данные
                    new_columns = window.data.columns.tolist()
                    for i, col in enumerate(required_columns):
                        if i < len(new_columns):
                            new_columns[i] = col
                    
                    # Спрашиваем пользователя о переименовании
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Icon.Question)
                    msg.setWindowTitle("Переименование колонок")
                    msg.setText("Отсутствуют необходимые колонки. Переименовать существующие?")
                    msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                    
                    if msg.exec() == QMessageBox.StandardButton.Yes:
                        window.data.columns = new_columns
                    else:
                        window.show_error_message(f"Отсутствуют необходимые колонки: {', '.join(missing_columns)}")
                        return
                else:
                    window.show_error_message(f"Отсутствуют необходимые колонки: {', '.join(missing_columns)}")
                    return
            
            # Преобразование колонки 'Урожайность' в числовой формат
            window.data['Урожайность'] = pd.to_numeric(window.data['Урожайность'], errors='coerce')
            
            # Проверка на пропущенные значения
            if window.data['Урожайность'].isna().any():
                window.show_error_message("В колонке 'Урожайность' обнаружены нечисловые значения, которые были заменены на NaN.")
                
                # Заполнение пропущенных значений средним
                window.data['Урожайность'].fillna(window.data['Урожайность'].mean(), inplace=True)
            
            # Отображение данных в таблице
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(window.data.columns.tolist())
            
            for row in window.data.itertuples(index=False):
                items = [QStandardItem(str(field)) for field in row]
                model.appendRow(items)
            
            window.DataTable.setModel(model)
            window.statusLabel.setText(f"Файл загружен: {file_path}")
            
            # Автоматическая настройка ширины колонок
            window.DataTable.resizeColumnsToContents()
            
        except Exception as e:
            window.show_error_message(f"Ошибка загрузки: {str(e)}")

    def save_data():
        """Сохраняет изменения в данных из таблицы"""
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
        
        # Преобразование колонки 'Урожайность' в числовой формат
        if 'Урожайность' in window.data.columns:
            window.data['Урожайность'] = pd.to_numeric(window.data['Урожайность'], errors='coerce')
        
        window.statusLabel.setText("Данные обновлены в памяти.")

    def export_data():
        """Экспортирует данные в CSV-файл"""
        if window.data is None:
            window.show_error_message("Нет данных для экспорта.")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            window, 
            "Сохранить как", 
            "", 
            "CSV Files (*.csv);;Excel Files (*.xlsx);;All Files (*.*)"
        )
        
        if not file_path:
            return
        
        try:
            # Определение формата по расширению
            if file_path.lower().endswith('.xlsx'):
                window.data.to_excel(file_path, index=False)
            else:
                # По умолчанию сохраняем как CSV
                if not file_path.lower().endswith('.csv'):
                    file_path += '.csv'
                window.data.to_csv(file_path, index=False)
            
            window.statusLabel.setText(f"Файл сохранён: {file_path}")
        except Exception as e:
            window.show_error_message(f"Ошибка при сохранении: {str(e)}")

    def add_sample_data():
        """Добавляет пример данных для тестирования"""
        # Создание примера данных
        varieties = ['Сорт A', 'Сорт B', 'Сорт C']
        fertilizers = ['Удобрение X', 'Удобрение Y', 'Удобрение Z']
        
        # Генерация случайных данных
        np.random.seed(42)  # Для воспроизводимости
        
        data = []
        for variety in varieties:
            for fertilizer in fertilizers:
                # Разные базовые значения для разных комбинаций
                base_yield = 20 + (varieties.index(variety) * 5) + (fertilizers.index(fertilizer) * 3)
                
                # Добавляем несколько наблюдений для каждой комбинации
                for _ in range(3):
                    yield_value = base_yield + np.random.normal(0, 2)
                    data.append([variety, fertilizer, round(yield_value, 2)])
        
        # Создание DataFrame
        window.data = pd.DataFrame(data, columns=['Сорт', 'Удобрение', 'Урожайность'])
        
        # Отображение данных в таблице
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(window.data.columns.tolist())
        
        for row in window.data.itertuples(index=False):
            items = [QStandardItem(str(field)) for field in row]
            model.appendRow(items)
        
        window.DataTable.setModel(model)
        window.statusLabel.setText("Загружены тестовые данные")
        
        # Автоматическая настройка ширины колонок
        window.DataTable.resizeColumnsToContents()

    # Подключение обработчиков событий
    window.LoadBtn.clicked.connect(load_data)
    window.SaveBtn.clicked.connect(save_data)
    window.ExportBtn.clicked.connect(export_data)
    
    # Добавление кнопки для создания тестовых данных
    if hasattr(window, 'SampleDataBtn'):
        window.SampleDataBtn.clicked.connect(add_sample_data)