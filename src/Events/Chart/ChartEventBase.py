from src.Chart import Chart

class ChartEventBase:
    chart: Chart

    def __init__(self, chart: Chart):
        self.chart = chart

    def on(self):
        pass

