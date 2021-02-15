from src import Timeframe, Chart

class TrendBase:
    timeframe: Timeframe
    force: int
    is_up: bool
    MAX_FORCE: 10
    MIN_FORCE: 1

    def __init__(self, chart: Chart, *args, **kwargs):
        self.chart = chart

    def calc_force(self) -> None:
        """
        TODO: reimplement in UpTrend and DownTrend
        """
        pass

