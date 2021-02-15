import DecisionStatus
from src.Strategy.TerminalOrders.OrderType import OrderType
from src.Strategy.TerminalOrders.CancelOrder import CancelOrder
from src.Strategy.TerminalOrders.BuyLimit import Bu

class MoveLimitOrder:
    ticker: str
    order_id: str
    order_type: OrderType
    volume: int
    price_prev: float
    price_to: float
    status: DecisionStatus

    def exec(self):
        co = CancelOrder(self.order_id)
        if (OrderType.buy == self.order_type):
            o = BuyLimit()
