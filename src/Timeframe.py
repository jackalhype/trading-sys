from enum import Enum

class Timeframe(Enum):
    m1 = 1
    m5 = 5
    m15 = 15
    m30 = 30
    h1 = 60
    h4 = 240
    d1 = 1440
    w1 = 'w1'
    mo1 = 'mo1'

