from .TerminalOrderBase import TerminalOrderBase

class SellMarket(TerminalOrderBase):
    time: float
    avg_price_exec: float

    def exec(self) -> str:
        pass
