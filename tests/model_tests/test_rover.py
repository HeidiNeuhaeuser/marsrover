import unittest
from marsrover.model.plateau import Plateau
from marsrover.model.rover import Rover


class TestRover(unittest.TestCase):
    def test_initialize(self):
        p = Plateau(5, 5)
        r = Rover(1, 2, 'N', p)
        rover_to_string = "{} {} {}".format(1, 2, 'N')
        self.assertEqual(str(r), rover_to_string)
