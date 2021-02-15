from src import Timeframe, Chart

class TrendBase:
    timeframe: Timeframe
    force: int
    MAX_FORCE: 10
    MIN_FORCE: 1

    def __init__(self, chart: Chart):
        self.chart = chart
        self.calc_force()

    def calc_force(self) -> None:
        pass

    