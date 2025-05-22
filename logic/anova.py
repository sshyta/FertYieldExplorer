import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd
import numpy as np
import scipy.stats as stats

def run_anova_analysis(data):
    """
    Проводит двухфакторный дисперсионный анализ (ANOVA) для определения влияния
    сорта культуры и типа удобрения на урожайность.
    
    Args:
        data (DataFrame): Данные с колонками 'Сорт', 'Удобрение', 'Урожайность'
        
    Returns:
        str: Результаты анализа в текстовом формате
    """
    try:
        # Проверка наличия необходимых колонок
        required_columns = ['Сорт', 'Удобрение', 'Урожайность']
        for col in required_columns:
            if col not in data.columns:
                return f"Ошибка: Отсутствует колонка '{col}' в данных"
        
        # Проверка типа данных
        if not pd.api.types.is_numeric_dtype(data['Урожайность']):
            return "Ошибка: Колонка 'Урожайность' должна содержать числовые значения"
        
        # Проведение двухфакторного дисперсионного анализа
        formula = 'Урожайность ~ C(Сорт) + C(Удобрение) + C(Сорт):C(Удобрение)'
        model = ols(formula, data=data).fit()
        anova_table = sm.stats.anova_lm(model, typ=2)
        
        # Расчет дополнительных статистик
        varieties = data['Сорт'].unique()
        fertilizers = data['Удобрение'].unique()
        
        # Расчет средних значений по группам
        group_means = data.groupby(['Сорт', 'Удобрение'])['Урожайность'].mean()
        
        # Форматирование результатов
        result = "РЕЗУЛЬТАТЫ ДВУХФАКТОРНОГО ДИСПЕРСИОННОГО АНАЛИЗА (ANOVA)\n"
        result += "=" * 70 + "\n\n"
        result += "Таблица дисперсионного анализа:\n"
        result += str(anova_table) + "\n\n"
        
        # Интерпретация результатов
        result += "ИНТЕРПРЕТАЦИЯ РЕЗУЛЬТАТОВ:\n"
        result += "-" * 70 + "\n"
        
        # Проверка влияния фактора "Сорт"
        p_variety = anova_table.loc['C(Сорт)', 'PR(>F)']
        result += f"Влияние фактора 'Сорт': "
        if p_variety < 0.05:
            result += f"Статистически значимо (p={p_variety:.4f})\n"
        else:
            result += f"Статистически не значимо (p={p_variety:.4f})\n"
        
        # Проверка влияния фактора "Удобрение"
        p_fertilizer = anova_table.loc['C(Удобрение)', 'PR(>F)']
        result += f"Влияние фактора 'Удобрение': "
        if p_fertilizer < 0.05:
            result += f"Статистически значимо (p={p_fertilizer:.4f})\n"
        else:
            result += f"Статистически не значимо (p={p_fertilizer:.4f})\n"
        
        # Проверка взаимодействия факторов
        p_interaction = anova_table.loc['C(Сорт):C(Удобрение)', 'PR(>F)']
        result += f"Взаимодействие факторов 'Сорт' и 'Удобрение': "
        if p_interaction < 0.05:
            result += f"Статистически значимо (p={p_interaction:.4f})\n"
        else:
            result += f"Статистически не значимо (p={p_interaction:.4f})\n"
        
        # Добавление средних значений по группам
        result += "\nСРЕДНИЕ ЗНАЧЕНИЯ УРОЖАЙНОСТИ ПО ГРУППАМ:\n"
        result += "-" * 70 + "\n"
        result += str(group_means.unstack()) + "\n"
        
        return result
    except Exception as e:
        return f"Ошибка при проведении ANOVA: {str(e)}"

def run_tukey_test(data):
    """
    Проводит post-hoc тест Тьюки (Tukey HSD) для определения, 
    какие конкретно группы статистически значимо отличаются друг от друга.
    
    Args:
        data (DataFrame): Данные с колонками 'Сорт', 'Удобрение', 'Урожайность'
        
    Returns:
        str: Результаты теста в текстовом формате
    """
    try:
        # Проверка наличия необходимых колонок
        required_columns = ['Сорт', 'Удобрение', 'Урожайность']
        for col in required_columns:
            if col not in data.columns:
                return f"Ошибка: Отсутствует колонка '{col}' в данных"
        
        # Проверка типа данных
        if not pd.api.types.is_numeric_dtype(data['Урожайность']):
            return "Ошибка: Колонка 'Урожайность' должна содержать числовые значения"
        
        # Создание комбинированной группы для теста Тьюки
        data['Группа'] = data['Сорт'] + " + " + data['Удобрение']
        
        # Проведение теста Тьюки
        tukey = pairwise_tukeyhsd(
            endog=data['Урожайность'],
            groups=data['Группа'],
            alpha=0.05
        )
        
        # Форматирование результатов
        result = "РЕЗУЛЬТАТЫ POST-HOC ТЕСТА ТЬЮКИ (TUKEY HSD)\n"
        result += "=" * 70 + "\n\n"
        result += str(tukey.summary()) + "\n\n"
        
        # Добавление интерпретации
        result += "ИНТЕРПРЕТАЦИЯ РЕЗУЛЬТАТОВ:\n"
        result += "-" * 70 + "\n"
        result += "Группы, для которых p-adj < 0.05, статистически значимо отличаются друг от друга.\n\n"
        
        # Выделение значимых различий
        significant_pairs = []
        for i, row in enumerate(tukey.summary().data[1:]):
            group1, group2, meandiff, p_adj = row[0], row[1], row[2], row[4]
            if p_adj < 0.05:
                significant_pairs.append((group1, group2, meandiff, p_adj))
        
        if significant_pairs:
            result += "СТАТИСТИЧЕСКИ ЗНАЧИМЫЕ РАЗЛИЧИЯ:\n"
            for group1, group2, meandiff, p_adj in significant_pairs:
                result += f"- {group1} vs {group2}: разница = {meandiff:.4f}, p = {p_adj:.4f}\n"
        else:
            result += "Не обнаружено статистически значимых различий между группами.\n"
        
        # Анализ по сортам
        result += "\nАНАЛИЗ ПО СОРТАМ:\n"
        result += "-" * 70 + "\n"
        for variety in data['Сорт'].unique():
            subset = data[data['Сорт'] == variety]
            if len(subset['Удобрение'].unique()) > 1:
                try:
                    variety_tukey = pairwise_tukeyhsd(
                        endog=subset['Урожайность'],
                        groups=subset['Удобрение'],
                        alpha=0.05
                    )
                    result += f"\nСорт: {variety}\n"
                    result += str(variety_tukey.summary()) + "\n"
                except:
                    result += f"\nСорт: {variety} - недостаточно данных для анализа\n"
        
        return result
    except Exception as e:
        return f"Ошибка при проведении теста Тьюки: {str(e)}"

def calculate_descriptive_stats(data):
    """
    Рассчитывает описательные статистики для данных.
    
    Args:
        data (DataFrame): Данные с колонками 'Сорт', 'Удобрение', 'Урожайность'
        
    Returns:
        str: Описательные статистики в текстовом формате
    """
    try:
        # Проверка наличия необходимых колонок
        if 'Урожайность' not in data.columns:
            return "Ошибка: Отсутствует колонка 'Урожайность' в данных"
        
        # Общие статистики
        overall_stats = data['Урожайность'].describe()
        
        # Статистики по сортам
        variety_stats = data.groupby('Сорт')['Урожайность'].describe()
        
        # Статистики по удобрениям
        fertilizer_stats = data.groupby('Удобрение')['Урожайность'].describe()
        
        # Форматирование результатов
        result = "ОПИСАТЕЛЬНЫЕ СТАТИСТИКИ\n"
        result += "=" * 70 + "\n\n"
        
        result += "ОБЩИЕ СТАТИСТИКИ:\n"
        result += "-" * 70 + "\n"
        result += str(overall_stats) + "\n\n"
        
        result += "СТАТИСТИКИ ПО СОРТАМ:\n"
        result += "-" * 70 + "\n"
        result += str(variety_stats) + "\n\n"
        
        result += "СТАТИСТИКИ ПО УДОБРЕНИЯМ:\n"
        result += "-" * 70 + "\n"
        result += str(fertilizer_stats) + "\n"
        
        return result
    except Exception as e:
        return f"Ошибка при расчете описательных статистик: {str(e)}"