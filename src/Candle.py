from datetime import datetime
from Timeframe import Timeframe

class Candle:
    open: float
    close: float
    high: float
    low: float
    volume: int
    start: datetime
    timeframe: Timeframe
    utc_offset: float

    
