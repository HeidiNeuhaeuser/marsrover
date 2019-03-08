import unittest
from marsrover.model.rover import Rover
from marsrover.model.direction import *

DIRECTIONS = get_directions()


class TestRover(unittest.TestCase):
    def test_initialize(self):

        r = Rover(1, 2, DIRECTIONS["N"], None)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.heading, DIRECTIONS["N"])

    def test_string(self):
        r = Rover(1, 2, 'N', None)
        rover_to_string = "{} {} {}".format(1, 2, 'N')
        self.assertEqual(str(r), rover_to_string)

    def test_turn_left(self):
        # TODO
        pass

    def test_turn_right(self):
        # TODO
        pass

    def test_move_forward(self):
        # TODO
        pass
