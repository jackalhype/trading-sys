from .TerminalOrderBase import TerminalOrderBase

class BuyMarket(TerminalOrderBase):
    time: float
    avg_price_exec: float

    def exec(self) -> str:
        pass