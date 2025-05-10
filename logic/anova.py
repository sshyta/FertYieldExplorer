import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def run_anova_analysis(data):
    try:
        model = ols('Урожайность ~ C(Сорт) + C(Удобрение) + C(Сорт):C(Удобрение)', data=data).fit()
        table = sm.stats.anova_lm(model, typ=2)
        return str(table)
    except Exception as e:
        return f"Ошибка ANOVA: {str(e)}"

def run_tukey_test(data):
    try:
        data['Группа'] = data['Сорт'] + "+" + data['Удобрение']
        tukey = pairwise_tukeyhsd(endog=data['Урожайность'], groups=data['Группа'], alpha=0.05)
        return str(tukey.summary())
    except Exception as e:
        return f"Ошибка Tukey HSD: {str(e)}"