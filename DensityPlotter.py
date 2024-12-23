# donut_chart.py
from xmlrpc.client import Boolean
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


class DensityPlotter:
    def __init__(self) -> None:
        self.image_dir = "images"
        print("DensityPlotter")

    def plot(self, data: dict, filename: str, fill: Boolean = True) -> None:
        sns.kdeplot(data, fill=fill, color='Blue')
        plt.xlabel("Value")
        plt.ylabel("Density")
        plt.title("Awesome Desity Plot")
        violin_filename: str = f"{self.image_dir}/{filename}"
        plt.savefig(violin_filename)


densityPlotter = DensityPlotter()

data = np.random.normal(size=1000)
densityPlotter.plot(data=data, filename="awesome_denisty_plot")
