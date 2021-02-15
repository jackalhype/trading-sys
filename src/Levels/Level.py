from src.Chart import Chart
from src.Timeframe import Timeframe
from datetime import datetime

class Level:
    # timeframe on which defined/recognized
    def_timeframe: Timeframe
    # determination start datetime
    start_dt: datetime
    # determination end datetime, None
    end_dt: datetime

    def __init__(self, chart: Chart, def_timeframe: Timeframe, start_dt: datetime, end_dt: datetime = None):
        self.chart = chart
        self.def_timeframe = def_timeframe
        self.start_dt = start_dt
        self.end_dt = end_dt

