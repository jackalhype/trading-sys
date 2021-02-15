import OrderStatus

class TerminalOrderBase:
    ticker: str
    status: OrderStatus
    order_id: str

    def exec(self) -> str:
        """
        TODO:
        returns: str, terminal order_id
        """
        self.order_id = None
        return self.order_id


