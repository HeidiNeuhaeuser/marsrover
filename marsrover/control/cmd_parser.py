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
        LOG.info(("Parsing input file '{}'.".format(self.input_file)))
        with open(self.input_file, 'r') as f:
            lines = list(filter(None, (line.rstrip() for line in f)))

        if not lines:
            raise ValueError("Input file empty.")

        command_invokers = []
        w, h = self._read_plateau_coords(lines[0])
        grid = Plateau(w, h)
        LOG.debug(("Plateau initialized with width={} and height={}.".format(w, h)))

        for i in range(1, len(lines), 2):
            x, y, d = self._read_rover_details(lines[i])
            mars_rover = Rover(x, y, d, grid)
            LOG.debug(("Rover initialized with x={}, y={} and d='{}'.".format(x, y, str(d))))
            command_invokers.append((mars_rover, self._read_commands(mars_rover, lines[i + 1])))

        return command_invokers

    @staticmethod
    def _read_plateau_coords(l):
        LOG.debug("Looking at line '{}' for plateau coordinates.".format(l))
        return list(map(int, l.rstrip().split()))

    @staticmethod
    def _read_rover_details(l):
        LOG.debug("Looking at line '{}' for rover details.".format(l))
        res = list(l.rstrip().split())
        if res[2] not in DIRECTIONS.keys():
            raise ValueError("Rover direction {} not supported.".format(res[2]))
        res[2] = DIRECTIONS[res[2]]
        return int(res[0]), int(res[1]), res[2]

    @staticmethod
    def _read_commands(r, l):
        c_invoker = CommandInvoker()
        LOG.debug("Looking at line '{}' for rover commands.".format(l))
        commands = {"L": TurnLeftCommand(r), "R": TurnRightCommand(r), "M": MoveForwardCommand(r)}

        for cmd in l:
            if cmd not in commands.keys():
                raise ValueError("Command {} not supported.".format(cmd))
            c_invoker.add_command(commands[cmd])

        LOG.debug("Commands added to command invoker.")

        return c_invoker
