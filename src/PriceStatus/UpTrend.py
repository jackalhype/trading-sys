import TrendBase
from src import Chart

class UpTrend(TrendBase):
    def __init__(self, *args, **kwargs):
        super(UpTrend, self).__init__(*args, **kwargs)

    def calc_force(self) -> int:
        pass

