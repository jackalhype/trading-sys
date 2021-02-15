from src.Levels import Level
from src import Chart

class LevelRetest:
    chart: Chart
    level: Level
    direction: int    # 1 up from bellow, -1 down from the top

    def __init__(self, chart: Chart, level: Level):
        self.chart = chart
        self.level = level

