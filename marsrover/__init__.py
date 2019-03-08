import argparse
import traceback
from marsrover.control.command import *
from marsrover.control.cmd_parser import CommandParser

LOG = logging.getLogger(os.path.basename(__file__))


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="marsrover")

    parser.add_argument(
        "-i",
        "--input",
        help="program input file.",
        required=False,
        default="sample_input.txt",
        dest="input_file")

    parser.add_argument(
        "-o",
        "--output",
        help="program output file.",
        required=False,
        default="sample_output.txt",
        dest="output_file")

    # Todo: FIx Logfile option

    return parser.parse_args()


def main():
    args = parse_arguments()
    c = CommandParser(args.input_file)

    try:
        command_invokers = c.parse()
    except Exception:
        LOG.error("Input file contains invalid input")
        LOG.error("Exit program!")
        traceback.print_exc()
        exit(1)

    for rover_invoker in command_invokers:
        rover, invoker = rover_invoker
        invoker.execute_commands()
        LOG.info("Rover Position after commands: {}".format(str(rover)))
        print("Rover Position after commands: {}".format(str(rover)))


if __name__ == "__main__":
    main()
