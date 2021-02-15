import DecisionBase
from src.Strategy.TerminalOrders.OrderType import OrderType
from src.Strategy.TerminalOrders.BuyLimit import BuyLimit
from src.Strategy.TerminalOrders.SellLimit import SellLimit
from src.Strategy.TerminalOrders.BuyStop import BuyStop
from src.Strategy.TerminalOrders.SellStop import SellStop

class PlaceOrder(DecisionBase):
    order_type: OrderType
    volume: int
    price: float
    stop_limit_price: float

    def __init__(self,
                order_type: OrderType,
                volume: int,
                price: float,
                stop_limit_price: float,
                *args, **kwargs):
        super(PlaceOrder, self).__init__(*args, **kwargs)
        self.order_type = order_type
        self.volume = volume
        self.price = price
        self.stop_limit_price = stop_limit_price

    def exec(self):
        if (OrderType.buy_limit == self.order_type):
            o = BuyLimit(volume=self.volume, price=self.price_to)
        elif (OrderType.sell_limit == self.order_type):
            o = SellLimit(volume=self.volume, price=self.price_to)
        elif (OrderType.buy_stop == self.order_type):
            o = BuyStop(volume=self.volume, price=self.price_to)
        elif (OrderType.sell_stop == self.order_type):
            o = SellStop(volume=self.volume, price=self.price_to)
        self.new_order_id = o.exec()

