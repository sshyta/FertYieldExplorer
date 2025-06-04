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
        
        def validate_data_quality(data):
            """Проверяет качество загруженных данных"""
            errors = []
            
            # Проверка на пустые данные
            if data.empty:
                errors.append("Файл не содержит данных")
                return errors
            
            # Проверка на минимальное количество строк
            if len(data) < 3:
                errors.append("Недостаточно данных для анализа (минимум 3 строки)")
            
            # Проверка колонки 'Сорт' на некорректные символы и пустые значения
            if 'Сорт' in data.columns:
                # Проверка на пустые значения
                if data['Сорт'].isna().any() or (data['Сорт'] == '').any():
                    errors.append("Колонка 'Сорт' содержит пустые значения")
                
                # Проверка на недопустимые символы (только буквы, цифры, пробелы, дефисы)
                invalid_chars = data['Сорт'].astype(str).str.contains(r'[^а-яА-Яa-zA-Z0-9\s\-]', na=False)
                if invalid_chars.any():
                    errors.append("Колонка 'Сорт' содержит недопустимые символы")
            
            # Проверка колонки 'Удобрение' на некорректные символы и пустые значения
            if 'Удобрение' in data.columns:
                # Проверка на пустые значения
                if data['Удобрение'].isna().any() or (data['Удобрение'] == '').any():
                    errors.append("Колонка 'Удобрение' содержит пустые значения")
                
                # Проверка на недопустимые символы
                invalid_chars = data['Удобрение'].astype(str).str.contains(r'[^а-яА-Яa-zA-Z0-9\s\-]', na=False)
                if invalid_chars.any():
                    errors.append("Колонка 'Удобрение' содержит недопустимые символы")
            
            # Проверка колонки 'Урожайность' на некорректные значения
            if 'Урожайность' in data.columns:
                # Проверка на пустые значения
                if data['Урожайность'].isna().any():
                    errors.append("Колонка 'Урожайность' содержит пустые значения")
                
                # Попытка преобразования в числовой формат
                numeric_data = pd.to_numeric(data['Урожайность'], errors='coerce')
                non_numeric_count = numeric_data.isna().sum()
                
                if non_numeric_count > 0:
                    errors.append(f"Колонка 'Урожайность' содержит {non_numeric_count} нечисловых значений")
                
                # Проверка на отрицательные значения
                if not numeric_data.isna().all():
                    negative_count = (numeric_data < 0).sum()
                    if negative_count > 0:
                        errors.append(f"Колонка 'Урожайность' содержит {negative_count} отрицательных значений")
                
                # Проверка на экстремально большие значения (больше 1000)
                if not numeric_data.isna().all():
                    extreme_count = (numeric_data > 1000).sum()
                    if extreme_count > 0:
                        errors.append(f"Колонка 'Урожайность' содержит {extreme_count} экстремально больших значений (>1000)")
            
            return errors
        
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
            
            # Валидация качества данных
            validation_errors = validate_data_quality(window.data)
            if validation_errors:
                error_message = "Обнаружены ошибки в данных:\n\n" + "\n".join([f"• {error}" for error in validation_errors])
                error_message += "\n\nПожалуйста, исправьте данные и попробуйте снова."
                window.show_error_message(error_message)
                return
            
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
            original_data = window.data['Урожайность'].copy()
            window.data['Урожайность'] = pd.to_numeric(window.data['Урожайность'], errors='coerce')

            # Детальная проверка на пропущенные значения
            nan_count = window.data['Урожайность'].isna().sum()
            if nan_count > 0:
                # Показываем какие именно значения были некорректными
                invalid_indices = window.data['Урожайность'].isna()
                invalid_values = original_data[invalid_indices].unique()
                
                error_message = f"В колонке 'Урожайность' обнаружено {nan_count} некорректных значений:\n"
                error_message += f"Некорректные значения: {', '.join(map(str, invalid_values[:10]))}"
                if len(invalid_values) > 10:
                    error_message += f" и еще {len(invalid_values) - 10}..."
                error_message += "\n\nЭти значения будут заменены на среднее значение."
                
                window.show_error_message(error_message)
                
                # Заполнение пропущенных значений средним
                mean_value = window.data['Урожайность'].mean()
                if pd.isna(mean_value):
                    window.show_error_message("Невозможно рассчитать среднее значение. Все данные урожайности некорректны.")
                    return
                
                window.data['Урожайность'].fillna(mean_value, inplace=True)
            
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