import argparse
import sys
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
        help="Determine input file.",
        required=False,
        default="sample_input.txt",
        dest="input_file")

    parser.add_argument(
        "-o",
        "--output",
        help="Determine output file.",
        required=False,
        default="sample_output.txt",
        dest="output_file")

    parser.add_argument(
        "-v",
        help="Print debug information.",
        required=False,
        default=False,
        dest="verbose")

    return parser.parse_args()


def main():
    args = parse_arguments()

    # configure logging
    log_level = logging.INFO
    if args.verbose:
        log_level = logging.DEBUG
    logging.basicConfig(
        stream=sys.stdout,
        level=log_level,
        format='[%(levelname)s]: (%(filename)s: line %(lineno)d) - %(message)s')

    c = CommandParser(args.input_file)

    try:
        command_invokers = c.parse()
    except Exception:
        LOG.error("Input file contains invalid input")
        LOG.error("Exit program!")
        traceback.print_exc()
        exit(1)

    out = args.output_file
    with open(out, 'w') as f:
        for rover_invoker in command_invokers:
            rover, invoker = rover_invoker
            invoker.execute_commands()
            LOG.info("Rover Position after commands: {}".format(str(rover)))
            f.write("{}\n".format(str(rover)))
        LOG.info("Output written into output file '{}'".format(out))


if __name__ == "__main__":
    main()
