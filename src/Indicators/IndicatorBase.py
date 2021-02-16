import os, sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.Timeframe import Timeframe

class IndicatorBase:
    ticker: str
    timeframe: Timeframe

    def __init__(self, ticker: str, timeframe: Timeframe):
        self.ticker = ticker
        self.timeframe = timeframe

