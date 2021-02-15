import TrendBase
from src import Chart

class DownTrend(TrendBase):
    def __init__(self, *args, **kwargs):
        super(DownTrend, self).__init__(*args, **kwargs)

    def calc_force(self) -> int:
        pass
