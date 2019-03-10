import unittest
from marsrover.model.rover import Rover
from marsrover.model.plateau import Plateau
from marsrover.model.direction import *

DIRECTIONS = get_directions()


class TestRover(unittest.TestCase):
    def test_initialize(self):

        r = Rover(1, 2, DIRECTIONS["N"], None)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.heading, DIRECTIONS["N"])
        self.assertEqual(r.heading.move[1], 1)

    def test_string(self):
        r = Rover(1, 2, DIRECTIONS["N"], None)
        rover_to_string = "{} {} {}".format(1, 2, 'N')
        self.assertEqual(str(r), rover_to_string)

    def test_turn_left(self):
        r = Rover(1, 2, DIRECTIONS["N"], None)
        r.turn_left()
        self.assertEqual(str(r.heading), str(DIRECTIONS["W"]))

    def test_turn_right(self):
        r = Rover(1, 2, DIRECTIONS["N"], None)
        r.turn_right()
        self.assertEqual(str(r.heading), str(DIRECTIONS["E"]))

    def test_move_forward(self):
        p = Plateau(5, 6)
        r = Rover(1, 2, DIRECTIONS["N"], p)
        r.move_forward()
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)


