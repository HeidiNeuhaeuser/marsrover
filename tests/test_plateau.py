import unittest
from marsrover.model.plateau import Plateau


class TestPlateau(unittest.TestCase):
    def test_initialize(self):
        p = Plateau(4, 7)
        self.assertEqual(p.width, 4)
        self.assertEqual(p.height, 7)

