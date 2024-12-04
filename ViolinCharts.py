# donut_chart.py
import matplotlib.pyplot as plt
import numpy as np


class ViolinCharts:
    def __init__(self):
        self.image_dir = 'images'
        print("ViolinCharts")

    def violin_plot(self, data, filename: str):
        plt.violinplot(data)
        plt.xlabel('Data')
        plt.ylabel('Density')
        plt.title('Awesome Violin Plot')
        violin_filename: str = f'{self.image_dir}/{filename}'
        plt.savefig(violin_filename)


violinCharts = ViolinCharts()

data = [np.random.normal(0, std, 100) for std in range(1, 4)]
violinCharts.violin_plot(data, 'awesome_violin_plot')
