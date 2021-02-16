from src.Strategy.TerminalOrders.BuyMarket import BuyMarket
from src.Strategy.TerminalOrders.SellMarket import SellMarket

# omg, there was so many vars in the 1st. And not even half finished.
# let's make it simple.
class Strat2:
    ticker: str
    min_deal_volume: int = 1
    is_trend_boolish: bool
    is_trend_bearish: bool
    have_good_price_to_open_buy: bool
    have_good_price_to_open_sell: bool
    bought: int = 0
    sold: int = 0

    def __init__(self, ticker: str):
        self.ticker = ticker

    def tryOpen(self):
        if self.is_trend_boolish:
            if self.have_good_price_to_open_buy:
                self.buy(volume=self.min_deal_volume)

        if self.is_trend_bearish:
            if self.have_good_price_to_open_sell:
                self.sell(volume=self.min_deal_volume)

    def buy(self, volume):
        new_sold = max(0, self.sold - volume)
        delta = volume - (self.sold - new_sold)
        self.sold = new_sold
        self.bought += delta
        BuyMarket(volume=volume).exec()


    def sell(self, volume):
        new_bought = max(0, self.bought - volume)
        delta = volume - (self.bought - new_bought)
        self.bought = new_bought
        self.sold += delta
        SellMarket(volume=volume).exec()

