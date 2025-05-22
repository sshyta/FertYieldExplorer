from logic.anova import run_anova_analysis, run_tukey_test, calculate_descriptive_stats
from PyQt6.QtWidgets import QMessageBox, QPushButton
from PyQt6.QtCore import QRect

def setup_analysis_page(window):
    """
    Настраивает страницу анализа данных.
    
    Args:
        window: Главное окно приложения
    """
    # Добавление нового типа анализа в выпадающий список
    window.testTypeCombo.clear()
    window.testTypeCombo.addItems(["ANOVA", "Tukey HSD", "Описательные статистики"])
    
    # Удаляем существующую кнопку экспорта результатов, если она уже есть
    if hasattr(window, 'exportResultsBtn') and window.exportResultsBtn is not None:
        try:
            window.exportResultsBtn.deleteLater()
        except:
            pass
    
    # Получаем геометрию кнопки запуска анализа для правильного позиционирования
    run_btn_geometry = window.runAnalysisBtn.geometry()
    
    # Создаем кнопку экспорта результатов и размещаем её точно под кнопкой запуска анализа
    window.exportResultsBtn = QPushButton("Экспорт результатов", window.analysisGroupBox)
    window.exportResultsBtn.setGeometry(
        run_btn_geometry.x(),  # Та же X-координата, что и у кнопки запуска
        run_btn_geometry.y() + run_btn_geometry.height() + 10,  # Y-координата: ниже кнопки запуска на 10 пикселей
        run_btn_geometry.width(),  # Та же ширина
        run_btn_geometry.height()  # Та же высота
    )
    
    def run_analysis():
        """Запускает выбранный тип статистического анализа"""
        if window.data is None:
            window.show_error_message("Сначала загрузите данные.")
            return

        # Получение выбранных параметров
        selected_test = window.testTypeCombo.currentText()
        crop_checked = window.cropFactorCheck.isChecked()
        fert_checked = window.fertilizerCheck.isChecked()
        inter_checked = window.interactionCheck.isChecked()

        # Проверка выбранных факторов
        if not (crop_checked or fert_checked):
            window.show_error_message("Выберите хотя бы один фактор для анализа.")
            return

        try:
            # Выполнение выбранного анализа
            if selected_test == "ANOVA":
                # ANOVA требует обязательно и сорт, и удобрение
                if not (crop_checked and fert_checked):
                    window.show_error_message("Для ANOVA необходимо выбрать и сорт, и тип удобрения.")
                    return
                
                result = run_anova_analysis(window.data)
                
            elif selected_test == "Tukey HSD":
                result = run_tukey_test(window.data)
                
            elif selected_test == "Описательные статистики":
                result = calculate_descriptive_stats(window.data)
                
            else:
                result = "Неверный выбор анализа."

            # Отображение результатов
            window.resultsText.setText(result)
            
        except Exception as e:
            error_message = f"Ошибка при выполнении анализа: {str(e)}"
            window.show_error_message(error_message)
            window.resultsText.setText(error_message)
    
    def export_results():
        """Экспортирует результаты анализа в текстовый файл"""
        from PyQt6.QtWidgets import QFileDialog
        
        if not window.resultsText.toPlainText():
            window.show_error_message("Нет результатов для экспорта.")
            return
        
        file_path, _ = QFileDialog.getSaveFileName(
            window, 
            "Сохранить результаты", 
            "analysis_results", 
            "Текстовые файлы (*.txt);;Все файлы (*.*)"
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(window.resultsText.toPlainText())
                window.statusLabel.setText(f"Результаты сохранены: {file_path}")
            except Exception as e:
                window.show_error_message(f"Ошибка при сохранении результатов: {str(e)}")
    
    # Подключение обработчиков событий
    window.runAnalysisBtn.clicked.connect(run_analysis)
    window.exportResultsBtn.clicked.connect(export_results)