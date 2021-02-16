from src.Timeframe import Timeframe
from src.Candle import Candle
from typing import List

class Chart:
    ticker: str
    timeframe: Timeframe
    candles: List[Candle]

    def __init__(self, ticker: str, timeframe: Timeframe, candles: List[Candle]):
        self.timeframe = timeframe
        self.candles = candles

    def appendCandle(self, candle: Candle):
        self.candles.append(candle)

