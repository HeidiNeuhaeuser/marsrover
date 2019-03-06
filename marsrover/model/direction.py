from enum import Enum, unique


@unique  # don't allow duplicate enum values
class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
