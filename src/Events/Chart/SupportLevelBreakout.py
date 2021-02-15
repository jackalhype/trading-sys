import ChartEventBase
from src.Levels import Level

# fall down the level
class SupportLevelBreakout(ChartEventBase):
    level: Level

    def __init__(self, level: Level):
        self.level = level

