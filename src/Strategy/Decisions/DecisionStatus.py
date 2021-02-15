from enum import Enum

class DecisionStatus(Enum):
    pending: 1
    success: 2
    unknown: 3
    partial: 4
    canceled: 6
    error: 9
