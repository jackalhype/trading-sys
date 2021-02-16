from src.Timeframe import Timeframe
from src.Chart import Chart
from src.Candle import Candle
from src.Strategy.PositionOpened import PositionOpened

import time
import sys

class ChartStatus:
    trend_direction: int # -1, 0, 1
    trend_strength: int # 1...10
    is_flat: bool
    is_uptrend: bool
    is_downtrend: bool
    is_parent_trend_codirectional: bool
    current_price_from_resistance: float
    current_price_from_support: float
    trade_comission: float
    position_opened: PositionOpened
    channel_depth: float

class UptrendChartStatus(ChartStatus):
    is_resistance_outbreak: bool
    is_going_retest: bool
    is_retest_confirmed: bool
    is_retest_failing: bool
    retest_failing_depth: float
    retest_failing_depth_percent: float

class DowntrendChartStatus(ChartStatus):
    is_support_outbreak: bool
    is_going_retest: bool

class Last3CandlesAnalytics:
    candle0: Candle     # current, drawing
    candle1: Candle     # previous
    candle2: Candle     # before previous
    candle3: Candle     # 3d into past lookout
    trade_comission: float



"""
Lets make it run during hours. Like the whole day. And the next day.
"""
class Strat1:
    ticker: str
    oper_timeframe: Timeframe
    parent_timeframe: Timeframe
    chart: Chart
    parent_chart: Chart
    chart_status: ChartStatus
    parent_chart_status: ChartStatus
    position_opened: PositionOpened

    def __init__(self, ticker: str):
        self.ticker = ticker
        self.oper_timeframe = Timeframe.m15
        self.parent_timeframe = Timeframe.h1

    def exec(self):
        while(True):
            try:
                self.getNewCandle()
                time.sleep(60)
            except:
                print("Unexpected error:", sys.exc_info()[0])

    def onNewCandleAppeared(self):
        self.chart_status = self.chartToStatus(self.chart)
        self.parent_chart_status = self.chartToStatus(self.parent_chart)



    def getNewCandle(self):
        """
        TODO
        """
        pass

    def chartToStatus(self, chart: Chart):
        pass

