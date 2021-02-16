from src.Indicators.IndicatorBase import IndicatorBase
from datetime import datetime

class MovingAverage(IndicatorBase):
    period: int

    def __init__(self, period: int, *args, **kwargs):
        super(MovingAverage, self).__init__(*args, **kwargs)
        self.period = period

    def getVal(self, dt: datetime) -> float:
        """
        TODO:
        :return:
        """
        pass

