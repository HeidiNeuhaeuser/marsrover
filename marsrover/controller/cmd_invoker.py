import logging
import os

LOG = logging.getLogger(os.path.basename(__file__))


class CommandInvoker:
    def __init__(self):
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()
