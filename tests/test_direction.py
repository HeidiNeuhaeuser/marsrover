import unittest
from marsrover.model.direction import *


class TestRover(unittest.TestCase):
    def test_initialize(self):
        d = Direction("W", "E", (2, 3), "N")
        self.assertEqual(d.left, "W")
        self.assertEqual(d.right, "E")
        self.assertEqual(d.move, (2, 3))
        self.assertEqual(d.move[0], 2)
        self.assertEqual(d.char, "N")

    def test_string(self):
        d = Direction("W", "E", (2, 3), "N")
        self.assertEqual(str(d), "N")

    def test_get_directions(self):
        dirs = get_directions()
        self.assertEqual(len(dirs), 4)
        self.assertEqual(dirs["S"].left, "E")
        self.assertEqual(dirs["S"].right, "W")
        self.assertEqual(dirs["S"].move, (0, -1))
        self.assertEqual(dirs["S"].char, "S")
