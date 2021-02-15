from enum import Enum

class OrderType(Enum):
    buy_limit = 'buy_limit'
    buy_market = 'buy_market'
    buy_stop = 'buy_stop'
    sell_limit = 'sell_limit'
    sell_market = 'sell_market'
    sell_stop = 'sell_stop'
