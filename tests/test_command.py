import unittest
from marsrover.control.command import *
from marsrover.model.rover import Rover


class TestCommand(unittest.TestCase):
    def test_initialize(self):
        r = Rover(2, 5, 'E', None)
        c1 = MoveForwardCommand(r)
        c2 = TurnRightCommand(r)
        c3 = TurnLeftCommand(r)

        self.assertEqual(c1._mars_rover, r)
        self.assertEqual(c2._mars_rover, r)
        self.assertEqual(c3._mars_rover, r)

    def test_turn_left_command(self):
        pass

    def test_turn_right_command(self):
        pass

    def test_move_forward_command(self):
        pass
