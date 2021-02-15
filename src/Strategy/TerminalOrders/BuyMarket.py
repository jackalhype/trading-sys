import TerminalOrderBase

class BuyMarket(TerminalOrderBase):
    lots: int
    time: float
    avg_price_exec: float

