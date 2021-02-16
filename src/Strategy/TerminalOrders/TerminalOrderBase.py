from .OrderStatus import OrderStatus

class TerminalOrderBase:
    ticker: str
    volume: int
    status: OrderStatus
    order_id: str

    def __init__(self, ticker: str, volume: int):
        self.ticker = ticker
        self.volume = volume

    def exec(self) -> str:
        """
        TODO:
        returns: str, terminal order_id
        """
        self.order_id = None
        return self.order_id


