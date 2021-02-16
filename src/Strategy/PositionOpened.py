class PositionOpened:
    ticker: str
    volume: int
    avg_price: float
    current_balance: float
    current_ticker_price: float
    is_long: bool
    is_short: bool
    is_valid_state: bool

    def __init__(self, ticker: str):
        self.ticker = ticker

    def setAttr(self,
                volume: int,
                avg_price: float,
                current_balance: float,
                current_ticker_price: float,
                is_long: bool,
                is_short: bool
            ) -> bool:
        """
        :param volume:
        :param avg_price:
        :param current_balance:
        :param current_ticker_price:
        :param is_long:
        :param is_short:
        :return:bool, is_valid_state
        """
        if volume is not None:
            self.volume = volume
        if avg_price is not None:
            self.avg_price = avg_price
        if current_balance is not None:
            self.current_balance = current_balance
        if current_ticker_price is not None:
            self.current_ticker_price = current_ticker_price
            
        self.is_valid_state = True
        if (self.volume > 0):
            if (bool == type(is_long)):
                self.is_long = is_long
                self.is_short = not is_long
            elif (bool == type(is_short)):
                self.is_short = is_short
                self.is_long = not is_short
            else:
                self.is_valid_state = False
        else:
            self.is_short = False
            self.is_long = False

        return self.is_valid_state
