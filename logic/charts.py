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
            # Создание точечного графика для каждого сорта
            for i, crop in enumerate(sorted(data['Сорт'].unique())):
                subset = data[data['Сорт'] == crop]
                # Добавляем небольшой разброс по оси X для лучшей визуализации
                x = np.arange(len(subset['Удобрение'].unique()))
                ax.scatter(x, subset['Урожайность'], 
                           label=crop, 
                           alpha=0.7,
                           s=80,
                           edgecolor='black')
            
            # Настройка оси X
            ax.set_xticks(np.arange(len(data['Удобрение'].unique())))
            ax.set_xticklabels(sorted(data['Удобрение'].unique()))
            
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

def create_interaction_plot(data):
    """
    Создает график взаимодействия между факторами.
    
    Args:
        data (DataFrame): Данные с колонками 'Сорт', 'Удобрение', 'Урожайность'
        
    Returns:
        Figure: Объект Figure с графиком взаимодействия
    """
    try:
        # Создание нового объекта Figure
        fig = Figure(figsize=(10, 6), dpi=100)
        ax = fig.add_subplot(111)
        
        # Группировка данных для графика взаимодействия
        interaction_data = data.groupby(['Сорт', 'Удобрение'])['Урожайность'].mean().reset_index()
        
        # Создание сводной таблицы
        pivot_table = interaction_data.pivot(index='Сорт', columns='Удобрение', values='Урожайность')
        
        # Построение графика взаимодействия
        for fertilizer in pivot_table.columns:
            ax.plot(pivot_table.index, pivot_table[fertilizer], 
                   marker='o', label=fertilizer, linewidth=2)
        
        ax.set_title('График взаимодействия: Сорт × Удобрение', fontsize=14, fontweight='bold')
        ax.set_xlabel('Сорт', fontsize=12)
        ax.set_ylabel('Средняя урожайность', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend(title='Удобрение')
        
        fig.tight_layout()
        return fig
    
    except Exception as e:
        print(f"Ошибка при создании графика взаимодействия: {str(e)}")
        return None

def export_chart(window):
    """
    Экспортирует текущий график в файл.
    
    Args:
        window: Главное окно приложения с доступом к данным и элементам интерфейса
    """
    from PyQt6.QtWidgets import QFileDialog
    
    # Определение текущего графика
    if window.chartsTabs.currentIndex() == 0:
        figure = window.figure1
        name = "main_chart"
    else:
        figure = window.figure2
        name = "comparison_chart"
    
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

def create_heatmap(data):
    """
    Создает тепловую карту корреляции между урожайностью, сортами и удобрениями.
    
    Args:
        data (DataFrame): Данные с колонками 'Сорт', 'Удобрение', 'Урожайность'
        
    Returns:
        Figure: Объект Figure с тепловой картой
    """
    try:
        # Создание нового объекта Figure
        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(111)
        
        # Создание сводной таблицы средней урожайности
        pivot_table = data.pivot_table(
            index='Сорт', 
            columns='Удобрение', 
            values='Урожайность',
            aggfunc='mean'
        )
        
        # Построение тепловой карты
        im = ax.imshow(pivot_table, cmap='YlGnBu')
        
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
                ax.text(j, i, f"{value:.2f}", ha="center", va="center", 
                       color="black" if value > pivot_table.values.mean() else "white")
        
        # Добавление цветовой шкалы
        cbar = fig.colorbar(im, ax=ax)
        cbar.set_label('Средняя урожайность')
        
        ax.set_title('Тепловая карта урожайности: Сорт × Удобрение', fontsize=14, fontweight='bold')
        fig.tight_layout()
        
        return fig
    
    except Exception as e:
        print(f"Ошибка при создании тепловой карты: {str(e)}")
        return None