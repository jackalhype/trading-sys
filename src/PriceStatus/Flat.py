from src.Levels import Level
from src import Chart

class Flat:
    chart: Chart
    upper_level: Level
    lower_level: Level

    def __init__(self, chart: Chart, upper_level: Level, lower_level: Level):
        self.chart = chart
        self.upper_level = upper_level
        self.lower_level = lower_level

