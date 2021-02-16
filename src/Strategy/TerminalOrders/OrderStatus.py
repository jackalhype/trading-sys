from enum import Enum

class OrderStatus(Enum):
    pending = 1
    success = 2
    unknown = 3
    canceled = 6
    error = 9
