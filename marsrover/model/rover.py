import logging
import os
from marsrover.model.direction import *

LOG = logging.getLogger(os.path.basename(__file__))
DIRECTIONS = get_directions()


class Rover:
    def __init__(self, x, y, h, p):
        self.x = x
        self.y = y
        self.heading = h
        self.plateau = p

    def __str__(self):
        return "{} {} {}".format(self.x, self.y, str(self.heading))

    def _check_move_legal(self):
        return (0 <= self.x + self.heading.move[0] <= self.plateau.width) and (
                0 <= self.y + self.heading.move[1] <= self.plateau.height)

    def move_forward(self):
        if self._check_move_legal() is True:
            self.x += self.heading.move[0]
            self.y += self.heading.move[1]
        else:
            LOG.error("Illegal move, rover cannot move out of plateau.")
            LOG.error("Exit program")
            exit(1)

    def turn_left(self):
        self.heading = DIRECTIONS[self.heading.left]

    def turn_right(self):
        self.heading = DIRECTIONS[self.heading.right]
