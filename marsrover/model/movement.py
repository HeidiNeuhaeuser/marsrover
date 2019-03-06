from enum import Enum, unique


@unique  # don't allow duplicate enum values
class Movement(Enum):
    L = 1
    R = 2
    M = 3
