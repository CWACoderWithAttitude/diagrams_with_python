# donut_chart.py
import plotly.express as px
import plotly.graph_objects as graph


class SunburstCharts:
    def __init__(self):
        self.image_dir = "images"
        print("SunburstCharts")

    def sunburst_charter(self, data: dict, filename: str):
        fig = px.sunburst(data, names="id", parents="parent", values="value")
        fig.update_layout(title_text="My Awesome Sunburst Chart")
        # fig.show() # debugging image generation
        fig.write_image(f"{self.image_dir}/{filename}", engine="kaleido")

    def bar_charter(self, labels: [], values: [], filename: str):
        fig = px.bar(x=labels, y=values)
        fig.update_layout(title_text="My Awesome Bar Chart")
        fig = fig.write_image(f"{self.image_dir}/{filename}")


sunburstCharts = SunburstCharts()

data = {
    "id": ["A", "B", "C", "D", "E", "F", "G"],
    "parent": ["", "A", "A", "B", "B", "C", "D"],
    "value": [10, 15, 7, 8, 12, 6, 5],
}

sunburstCharts.sunburst_charter(data=data, filename="awesome_sunburst.png")
sunburstCharts.bar_charter(
    data["id"], data["value"], filename="awesome_bar-chart.png")
