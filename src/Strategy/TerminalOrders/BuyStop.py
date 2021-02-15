import TerminalOrderBase

class BuyStop(TerminalOrderBase):
    volume: int
    price: float
    