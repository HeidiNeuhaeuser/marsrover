import unittest
from marsrover.control.command import *
from marsrover.model.rover import Rover
from marsrover.model.plateau import Plateau
from marsrover.model.direction import *

DIRECTIONS = get_directions()


class TestCommand(unittest.TestCase):
    def test_initialize(self):
        r = Rover(2, 5, DIRECTIONS["E"], None)
        c1 = MoveForwardCommand(r)
        c2 = TurnRightCommand(r)
        c3 = TurnLeftCommand(r)

        self.assertEqual(c1._mars_rover, r)
        self.assertEqual(c2._mars_rover, r)
        self.assertEqual(c3._mars_rover, r)

    def test_turn_left_command(self):
        p = Plateau(5, 6)
        r = Rover(2, 5, DIRECTIONS["E"], p)
        c = TurnLeftCommand(r)

        c.execute()
        self.assertEqual(str(r.heading), str(DIRECTIONS["N"]))

    def test_turn_right_command(self):
        p = Plateau(5, 6)
        r = Rover(2, 5, DIRECTIONS["E"], p)
        c = TurnRightCommand(r)

        c.execute()
        self.assertEqual(str(r.heading), str(DIRECTIONS["S"]))

    def test_move_forward_command(self):
        p = Plateau(5, 6)
        r = Rover(2, 5, DIRECTIONS["E"], p)
        c = MoveForwardCommand(r)

        c.execute()
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 5)

