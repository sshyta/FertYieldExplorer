import matplotlib.pyplot as plt

def update_main_chart(window):
    if window.data is None:
        return
    window.figure1.clear()
    ax = window.figure1.add_subplot(111)
    chart_type = window.chartTypeCombo.currentText()
    data = window.data

    try:
        if chart_type == "Столбчатая":
            avg_data = data.groupby('Сорт')['Урожайность'].mean()
            ax.bar(avg_data.index, avg_data.values, color='skyblue')
            ax.set_title('Средняя урожайность по сортам')
        elif chart_type == "Ящик с усами":
            data_to_plot = [data[data['Удобрение'] == f]['Урожайность'] for f in data['Удобрение'].unique()]
            ax.boxplot(data_to_plot, labels=data['Удобрение'].unique())
            ax.set_title('Урожайность по удобрениям')
        elif chart_type == "Точечная":
            for crop in data['Сорт'].unique():
                subset = data[data['Сорт'] == crop]
                ax.scatter(subset['Удобрение'], subset['Урожайность'], label=crop)
            ax.legend()
            ax.set_title('Урожайность по сортам и удобрениям')

        if window.showTrendCheck.isChecked():
            mean_yield = data['Урожайность'].mean()
            ax.axhline(mean_yield, color='red', linestyle='--', label='Среднее')
            ax.legend()

        window.canvas1.draw()
    except Exception as e:
        window.show_error_message(f"Ошибка графика: {str(e)}")

def update_comparison_chart(window):
    if window.data is None:
        return
    window.figure2.clear()
    ax = window.figure2.add_subplot(111)

    try:
        if window.radioButton.isChecked():
            pivot = window.data.pivot_table(index='Удобрение', columns='Сорт', values='Урожайность')
        else:
            pivot = window.data.pivot_table(index='Сорт', columns='Удобрение', values='Урожайность')
        pivot.plot(kind='bar', ax=ax)
        ax.set_ylabel('Урожайность')
        window.canvas2.draw()
    except Exception as e:
        window.show_error_message(f"Ошибка сравнения: {str(e)}")

def export_chart(window):
    from PyQt6.QtWidgets import QFileDialog
    if window.chartsTabs.currentIndex() == 0:
        figure = window.figure1
        name = "main_chart"
    else:
        figure = window.figure2
        name = "comparison_chart"

    file_path, _ = QFileDialog.getSaveFileName(window, "Сохранить", name, "PNG (*.png);;PDF (*.pdf);;SVG (*.svg)")
    if file_path:
        try:
            figure.savefig(file_path, dpi=300)
            window.statusLabel.setText(f"Сохранено: {file_path}")
        except Exception as e:
            window.show_error_message(f"Ошибка сохранения: {str(e)}")