import OrderStatus

class CancelOrder:
    order_id: str
    status: OrderStatus

    def __init__(self, order_id: str):
        if not order_id:
            raise ValueError("Empty order_id")
        self.order_id = order_id

    def exec(self):
        """
        TODO:
        """
        pass