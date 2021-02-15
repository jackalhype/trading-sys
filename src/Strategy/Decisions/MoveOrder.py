import DecisionBase
from src.Strategy.TerminalOrders.OrderType import OrderType
from src.Strategy.TerminalOrders.CancelOrder import CancelOrder
from src.Strategy.TerminalOrders.BuyLimit import BuyLimit
from src.Strategy.TerminalOrders.SellLimit import SellLimit
from src.Strategy.TerminalOrders.BuyStop import BuyStop
from src.Strategy.TerminalOrders.SellStop import SellStop

class MoveOrder(DecisionBase):
    order_id: str
    price_to: float
    new_order_id: str
    order_type: OrderType
    volume: int
    price_prev: float

    def __init__(self, order_id: str, price_to: float, *args, **kwargs):
        self.order_id = order_id
        self.price_to = price_to
        super(MoveOrder, self).__init__(*args, **kwargs)

    def exec(self):
        co = CancelOrder(self.order_id)
        co.exec()
        if (OrderType.buy_limit == self.order_type):
            o = BuyLimit(volume=self.volume, price=self.price_to)
        elif (OrderType.sell_limit == self.order_type):
            o = SellLimit(volume=self.volume, price=self.price_to)
        elif (OrderType.buy_stop == self.order_type):
            o = BuyStop(volume=self.volume, price=self.price_to)
        elif (OrderType.sell_stop == self.order_type):
            o = SellStop(volume=self.volume, price=self.price_to)
        self.new_order_id = o.exec()

