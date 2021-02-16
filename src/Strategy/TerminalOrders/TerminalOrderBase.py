from .OrderStatus import OrderStatus

class TerminalOrderBase:
    ticker: str
    status: OrderStatus
    order_id: str

    def __init__(self, ticker: str):
        self.ticker = ticker

    def exec(self) -> str:
        """
        TODO:
        returns: str, terminal order_id
        """
        self.order_id = None
        return self.order_id


