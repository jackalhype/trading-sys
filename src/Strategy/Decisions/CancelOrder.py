import DecisionBase
from src.Strategy.TerminalOrders.CancelOrder import CancelOrder as TCO

class CancelOrder(DecisionBase):
    order_id: str

    def __init__(self, order_id: str, *args, **kwargs):
        super(CancelOrder, self).__init__(*args, **kwargs)
        self.order_id = order_id

    def exec(self):
        o = TCO(order_id=self.order_id)
        o.exec()
