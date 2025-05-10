from logic.anova import run_anova_analysis, run_tukey_test

def setup_analysis_page(window):
    def run_analysis():
        if window.data is None:
            window.show_error_message("Сначала загрузите данные.")
            return

        if window.testTypeCombo.currentText() == "ANOVA":
            result = run_anova_analysis(window.data)
        elif window.testTypeCombo.currentText() == "Tukey HSD":
            result = run_tukey_test(window.data)
        else:
            result = "Неверный выбор анализа."
        window.resultsText.setText(result)

    window.runAnalysisBtn.clicked.connect(run_analysis)