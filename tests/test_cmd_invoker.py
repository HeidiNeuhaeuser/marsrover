import unittest
from marsrover.control.cmd_invoker import CommandInvoker
from marsrover.control.command import *
from marsrover.model.rover import Rover
from marsrover.model.plateau import Plateau
from marsrover.model.direction import *


DIRECTIONS = get_directions()


class TestCommandInvoker(unittest.TestCase):
    def test_initialize(self):
        ci = CommandInvoker()
        self.assertEqual(ci._commands, [])

    def test_add_command(self):
        ci = CommandInvoker()
        cmd1 = TurnRightCommand(None)

        ci.add_command(cmd1)
        self.assertEqual(len(ci._commands), 1)
        self.assertIsInstance(ci._commands[0], TurnRightCommand)

    def test_execute_commands(self):
        p = Plateau(5, 6)
        r = Rover(1, 2, DIRECTIONS["N"], p)
        ci = CommandInvoker()
        cmd1 = MoveForwardCommand(r)

        ci.add_command(cmd1)
        ci.execute_commands()
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)

