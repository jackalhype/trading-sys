import DecisionStatus

class DecisionBase:
    ticker: str
    status: DecisionStatus

    def __init__(self, ticker: str, *args, **kwargs):
        self.ticker = ticker

    def refresh_status(self):
        """
        TODO
        check terminal
        """
        pass
