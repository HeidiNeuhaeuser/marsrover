import logging
import os
import abc

LOG = logging.getLogger(os.path.basename(__file__))


class Command(metaclass=abc.ABCMeta):
    # base class for commands
    def __init__(self, r):
        self._mars_rover = r

    @abc.abstractmethod
    def execute(self):
        pass


class MoveForwardCommand(Command):
    def execute(self):
        self._mars_rover.move_forward()


class TurnLeftCommand(Command):
    def execute(self):
        self._mars_rover.turn_left()


class TurnRightCommand(Command):
    def execute(self):
        self._mars_rover.turn_right()
