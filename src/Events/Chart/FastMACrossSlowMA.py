from src.Indicators.MovingAverage import MovingAverage
import ChartEventBase
from src.Candle import Candle

class FastMACrossSlowMA(ChartEventBase):
    fastMA: MovingAverage
    slowMA: MovingAverage
    direction: int      # 1 up, -1 down
    candle: Candle

