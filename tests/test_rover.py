import unittest
from marsrover.model.rover import Rover


class TestRover(unittest.TestCase):
    def test_initialize(self):
        r = Rover(1, 2, 'N', None)
        rover_to_string = "{} {} {}".format(1, 2, 'N')
        self.assertEqual(str(r), rover_to_string)
