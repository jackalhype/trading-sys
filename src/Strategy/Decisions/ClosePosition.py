from DecisionBase import DecisionBase
from CancelOrder import CancelOrder
from typing import List

class ClosePosition(DecisionBase):
    order_ids: List[str]

    def __init__(self, *args, **kwargs):
        super(ClosePosition, self).__init__(*args, **kwargs)
        """
        TODO:
        self.order_ids =         
        """

    def exec(self):
        for order_id in self.order_ids:
            co = CancelOrder(order_id)
            co.exec()
