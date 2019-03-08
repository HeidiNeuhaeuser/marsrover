import logging
import os

LOG = logging.getLogger(os.path.basename(__file__))


class Rover:
    def __init__(self, x, y, h, p):
        self.x = x
        self.y = y
        self.heading = h
        self.plateau = p

    def __str__(self):
        return "{} {} {}".format(self.x, self.y, self.heading)

    def check_move_legal(self):
        pass

    def move_forward(self):
        # TODO check if move legal (plateau)
        print("moving forward")

    def turn_left(self):
        pass

    def turn_right(self):
        pass
