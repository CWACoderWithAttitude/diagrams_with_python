# donut_chart.py
import matplotlib.pyplot as plt


class DonutCharts:
    def __init__(self):
        self.image_dir = "images"
        print("DonutCharts")

    def donut_charter(
        self, sizes, labels, filename: str
    ):
        plt.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
        )
        circle = plt.Circle(
            (0, 0), 0.8, color="white"
        )
        plt.gca().add_artist(circle)
        plt.title("Donut Chat")
        donut_filename: str = (
            f"{self.image_dir}/{filename}.png"
        )
        plt.savefig(donut_filename)


donnutCharts = DonutCharts()

sizes = [15, 30, 45, 10]
labels = ["A", "B", "C", "D"]
donnutCharts.donut_charter(
    sizes, labels, "donut_chart"
)
