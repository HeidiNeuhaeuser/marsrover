import unittest
from marsrover.control.cmd_parser import CommandParser
from marsrover.control.command import *
from marsrover.model.direction import *


DIRECTIONS = get_directions()


class TestCommandParser(unittest.TestCase):
    def test_initialize(self):
        c = CommandParser("input.txt")
        self.assertEqual(c.input_file, "input.txt")

    def test_read_plateau_coords(self):
        cp = CommandParser(None)
        s = "5 7"
        a, b = cp._read_plateau_coords(s)

        self.assertEqual(a, 5)
        self.assertEqual(b, 7)

    def test_read_rover_details(self):
        cp = CommandParser(None)
        s = "4 7 N"
        x, y, d = cp._read_rover_details(s)

        self.assertEqual(x, 4)
        self.assertEqual(y, 7)
        self.assertEqual(str(d), str(DIRECTIONS['N']))

    def test__read_commands(self):
        cp = CommandParser(None)
        s = "LMR"
        invoker = cp._read_commands(None, s)

        self.assertEqual(len(invoker._commands), 3)
        self.assertIsInstance(invoker._commands[0], TurnLeftCommand)
        self.assertIsInstance(invoker._commands[1], MoveForwardCommand)
        self.assertIsInstance(invoker._commands[2], TurnRightCommand)
