from marsrover.model.rover import Rover
from marsrover.model.plateau import Plateau
from marsrover.model.direction import *
from marsrover.control.cmd_invoker import CommandInvoker
from marsrover.control.command import *

LOG = logging.getLogger(os.path.basename(__file__))
DIRECTIONS = get_directions()


class CommandParser:
    def __init__(self, i):
        self.input_file = i

    def parse(self):
        with open(self.input_file, 'r') as f:
            lines = f.readlines()

        # TODO: check empty input
        command_invokers = []
        w, h = self._read_plateau_coords(lines[0])
        grid = Plateau(w, h)

        for i in range(1, len(lines), 2):
            x, y, d = self._read_rover_details(lines[i])
            if not DIRECTIONS[d]:
                LOG.error("Rover direction {} not supported.".format(d))
                LOG.error("Exit program!")
                exit(1)
            d = DIRECTIONS[d]
            mars_rover = Rover(x, y, d, grid)
            command_invokers.append((mars_rover, self._read_commands(mars_rover, lines[i + 1])))

        return command_invokers

    @staticmethod
    def _read_plateau_coords(self, l):
        return list(map(int, l.rstrip().split()))

    @staticmethod
    def _read_rover_details(self, l):
        res = list(l.rstrip().split())
        return int(res[0]), int(res[1]), res[2]

    @staticmethod
    def _read_commands(self, r, l):
        c_invoker = CommandInvoker()
        commands = {"L" : TurnLeftCommand(r), "R": TurnRightCommand(r), "M" : MoveForwardCommand(r)}

        for cmd in l:
            if commands[cmd]:
                c_invoker.add_command(commands[cmd])

        return c_invoker
