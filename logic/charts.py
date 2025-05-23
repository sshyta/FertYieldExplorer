import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib.figure import Figure

def update_main_chart(window):
    """
    Обновляет основной график в зависимости от выбранного типа.
    
    Args:
        window: Главное окно приложения с доступом к данным и элементам интерфейса
    """
    if window.data is None:
        window.show_error_message("Нет данных для построения графика")
        return
    
    try:
        window.figure1.clear()
        ax = window.figure1.add_subplot(111)
        chart_type = window.chartTypeCombo.currentText()
        data = window.data
        
        # Проверка наличия необходимых колонок
        required_columns = ['Сорт', 'Удобрение', 'Урожайность']
        for col in required_columns:
            if col not in data.columns:
                window.show_error_message(f"Отсутствует колонка '{col}' в данных")
                return
        
        # Построение графика в зависимости от выбранного типа
        if chart_type == "Столбчатая":
            # Группировка данных по сортам и расчет средней урожайности
            avg_data = data.groupby('Сорт')['Урожайность'].mean().sort_values(ascending=False)
            bars = ax.bar(avg_data.index, avg_data.values, color='skyblue', edgecolor='navy')
            
            # Добавление значений над столбцами
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                        f'{height:.2f}', ha='center', va='bottom')
            
            ax.set_title('Средняя урожайность по сортам', fontsize=12, fontweight='bold')
            ax.set_xlabel('Сорт', fontsize=10)
            ax.set_ylabel('Средняя урожайность', fontsize=10)
            ax.grid(axis='y', linestyle='--', alpha=0.7)
            
        elif chart_type == "Ящик с усами":
            # Создание ящиков с усами для каждого удобрения
            sns.boxplot(x='Удобрение', y='Урожайность', data=data, ax=ax, palette='Set3')
            
            ax.set_title('Распределение урожайности по удобрениям', fontsize=12, fontweight='bold')
            ax.set_xlabel('Тип удобрения', fontsize=10)
            ax.set_ylabel('Урожайность', fontsize=10)
            ax.grid(axis='y', linestyle='--', alpha=0.7)
            
        elif chart_type == "Точечная":
            # Исправленная точечная диаграмма
            fertilizers = sorted(data['Удобрение'].unique())
            varieties = sorted(data['Сорт'].unique())
            
            # Создание числовых позиций для удобрений
            fertilizer_positions = {fert: i for i, fert in enumerate(fertilizers)}
            
            # Построение точек для каждого сорта
            for variety in varieties:
                subset = data[data['Сорт'] == variety]
                
                # Получение позиций X и значений Y
                x_positions = [fertilizer_positions[fert] for fert in subset['Удобрение']]
                y_values = subset['Урожайность'].values
                
                # Добавление небольшого случайного смещения для лучшей видимости
                x_jitter = np.random.normal(0, 0.05, len(x_positions))
                x_final = np.array(x_positions) + x_jitter
                
                ax.scatter(x_final, y_values, 
                          label=variety, 
                          alpha=0.7,
                          s=80,
                          edgecolor='black')
            
            # Настройка оси X
            ax.set_xticks(range(len(fertilizers)))
            ax.set_xticklabels(fertilizers)
            
            ax.set_title('Урожайность по сортам и удобрениям', fontsize=12, fontweight='bold')
            ax.set_xlabel('Тип удобрения', fontsize=10)
            ax.set_ylabel('Урожайность', fontsize=10)
            ax.grid(True, linestyle='--', alpha=0.7)
            ax.legend(title='Сорт')
        
        # Добавление линии тренда, если выбрано
        if window.showTrendCheck.isChecked():
            mean_yield = data['Урожайность'].mean()
            ax.axhline(mean_yield, color='red', linestyle='--', 
                      label=f'Среднее ({mean_yield:.2f})')
            ax.legend()
        
        # Настройка внешнего вида графика
        window.figure1.tight_layout()
        window.canvas1.draw()
        
    except Exception as e:
        window.show_error_message(f"Ошибка при построении графика: {str(e)}")

def update_comparison_chart(window):
    """
    Обновляет график сравнения в зависимости от выбранной группировки.
    
    Args:
        window: Главное окно приложения с доступом к данным и элементам интерфейса
    """
    if window.data is None:
        return
    
    try:
        window.figure2.clear()
        ax = window.figure2.add_subplot(111)
        data = window.data
        
        # Проверка наличия необходимых колонок
        required_columns = ['Сорт', 'Удобрение', 'Урожайность']
        for col in required_columns:
            if col not in data.columns:
                window.show_error_message(f"Отсутствует колонка '{col}' в данных")
                return
        
        # Группировка данных в зависимости от выбранного переключателя
        if window.radioButton.isChecked():  # Группировка по сортам
            # Создаем сводную таблицу: строки - удобрения, столбцы - сорта
            pivot = data.pivot_table(
                index='Удобрение', 
                columns='Сорт', 
                values='Урожайность',
                aggfunc='mean'
            )
            
            # Построение графика
            pivot.plot(kind='bar', ax=ax, width=0.8)
            ax.set_title('Сравнение урожайности по сортам для каждого удобрения', 
                        fontsize=12, fontweight='bold')
            ax.set_xlabel('Тип удобрения', fontsize=10)
            
        else:  # Группировка по удобрениям
            # Создаем сводную таблицу: строки - сорта, столбцы - удобрения
            pivot = data.pivot_table(
                index='Сорт', 
                columns='Удобрение', 
                values='Урожайность',
                aggfunc='mean'
            )
            
            # Построение графика
            pivot.plot(kind='bar', ax=ax, width=0.8)
            ax.set_title('Сравнение урожайности по удобрениям для каждого сорта', 
                        fontsize=12, fontweight='bold')
            ax.set_xlabel('Сорт', fontsize=10)
        
        ax.set_ylabel('Средняя урожайность', fontsize=10)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        ax.legend(title='Легенда')
        
        # Настройка внешнего вида графика
        window.figure2.tight_layout()
        window.canvas2.draw()
        
    except Exception as e:
        window.show_error_message(f"Ошибка при построении графика сравнения: {str(e)}")

def create_interaction_plot(window):
    """
    Создает график взаимодействия между факторами прямо на canvas.
    
    Args:
        window: Главное окно приложения с доступом к данным
    """
    try:
        # Очищаем фигуру
        window.figure3.clear()
        ax = window.figure3.add_subplot(111)
        
        data = window.data
        
        # Группировка данных для графика взаимодействия
        interaction_data = data.groupby(['Сорт', 'Удобрение'])['Урожайность'].mean().reset_index()
        
        # Создание сводной таблицы
        pivot_table = interaction_data.pivot(index='Сорт', columns='Удобрение', values='Урожайность')
        
        # Построение графика взаимодействия
        for fertilizer in pivot_table.columns:
            ax.plot(pivot_table.index, pivot_table[fertilizer], 
                   marker='o', label=fertilizer, linewidth=2, markersize=8)
        
        ax.set_title('График взаимодействия: Сорт × Удобрение', fontsize=14, fontweight='bold')
        ax.set_xlabel('Сорт', fontsize=12)
        ax.set_ylabel('Средняя урожайность', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend(title='Удобрение')
        
        # Поворот меток по оси X для лучшей читаемости
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
        
        window.figure3.tight_layout()
        window.canvas3.draw()
        
        return True
    
    except Exception as e:
        print(f"Ошибка при создании графика взаимодействия: {str(e)}")
        return False

def create_heatmap(window):
    """
    Создает тепловую карту прямо на canvas.
    
    Args:
        window: Главное окно приложения с доступом к данным
    """
    try:
        # Очищаем фигуру
        window.figure4.clear()
        ax = window.figure4.add_subplot(111)
        
        data = window.data
        
        # Создание сводной таблицы средней урожайности
        pivot_table = data.pivot_table(
            index='Сорт', 
            columns='Удобрение', 
            values='Урожайность',
            aggfunc='mean'
        )
        
        # Построение тепловой карты
        im = ax.imshow(pivot_table.values, cmap='YlGnBu', aspect='auto')
        
        # Настройка осей
        ax.set_xticks(np.arange(len(pivot_table.columns)))
        ax.set_yticks(np.arange(len(pivot_table.index)))
        ax.set_xticklabels(pivot_table.columns)
        ax.set_yticklabels(pivot_table.index)
        
        # Поворот меток по оси X для лучшей читаемости
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
        
        # Добавление значений в ячейки
        for i in range(len(pivot_table.index)):
            for j in range(len(pivot_table.columns)):
                value = pivot_table.iloc[i, j]
                if not pd.isna(value):
                    text_color = "white" if value < pivot_table.values.mean() else "black"
                    ax.text(j, i, f"{value:.2f}", ha="center", va="center", 
                           color=text_color, fontweight='bold')
        
        # Добавление цветовой шкалы
        cbar = window.figure4.colorbar(im, ax=ax)
        cbar.set_label('Средняя урожайность', fontsize=10)
        
        ax.set_title('Тепловая карта урожайности: Сорт × Удобрение', fontsize=14, fontweight='bold')
        
        window.figure4.tight_layout()
        window.canvas4.draw()
        
        return True
    
    except Exception as e:
        print(f"Ошибка при создании тепловой карты: {str(e)}")
        return False

def export_chart(window):
    """
    Экспортирует текущий график в файл.
    
    Args:
        window: Главное окно приложения с доступом к данным и элементам интерфейса
    """
    from PyQt6.QtWidgets import QFileDialog
    
    # Определение текущего графика
    current_tab = window.chartsTabs.currentIndex()
    if current_tab == 0:
        figure = window.figure1
        name = "main_chart"
    elif current_tab == 1:
        figure = window.figure2
        name = "comparison_chart"
    elif current_tab == 2:
        figure = window.figure3
        name = "interaction_chart"
    elif current_tab == 3:
        figure = window.figure4
        name = "heatmap_chart"
    else:
        figure = window.figure1
        name = "chart"
    
    # Диалог сохранения файла
    file_path, _ = QFileDialog.getSaveFileName(
        window, 
        "Сохранить график", 
        name, 
        "PNG (*.png);;PDF (*.pdf);;SVG (*.svg);;JPEG (*.jpg)"
    )
    
    if file_path:
        try:
            # Сохранение графика с высоким разрешением
            figure.savefig(file_path, dpi=300, bbox_inches='tight')
            window.statusLabel.setText(f"График сохранен: {file_path}")
        except Exception as e:
            window.show_error_message(f"Ошибка при сохранении графика: {str(e)}")