#!/usr/bin/env python

from Timeframe import Timeframe

# We have to monitor short term changes in price of all the Market.
class MarketSituation:
    sources = ('yahoo_api', 'yahoo_html')

    def __init__(self):
        pass

    def sync(self, source: str):
        pass

    def getMarketDirectionTensor(self, timeframe : Timeframe):
        """
        scale -10...+10
        (m1,

        """


