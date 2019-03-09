import argparse
import sys
from marsrover.control.command import *
from marsrover.control.cmd_parser import CommandParser

LOG = logging.getLogger(os.path.basename(__file__))
# TODO: Tests and comments


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="marsrover")

    parser.add_argument(
        "-i",
        help="Determine input file.",
        required=True,
        default="sample_input.txt",
        dest="input_file")

    parser.add_argument(
        "-o",
        help="Determine output file name.",
        required=False,
        default="sample_output.txt",
        dest="output_file")

    parser.add_argument(
        "-v",
        help="Print debug information.",
        required=False,
        default=False,
        dest="verbose",
        action="store_true"
    )

    return parser.parse_args()


def configure_logging(args_log_level):
    log_level = logging.INFO
    if args_log_level:
        log_level = logging.DEBUG

    logging.basicConfig(
        stream=sys.stdout,
        level=log_level,
        format='[%(levelname)s]: (%(filename)s: line %(lineno)d) - %(message)s')


def check_input_file(i):
    if not os.path.isfile(i):
        exit_program("Input file does not exist in directory.")


def write_output_file(file_name, content):
    out = "marsrover_output.txt"
    if file_name:
        out = file_name

    with open(out, 'w') as f:
        f.write(content)
    LOG.info("Output written into file '{}'".format(out))


def print_welcome():
    print("\n*** WELCOME TO MARS ROVER ***\n")


def print_bye():
    print("\n*** BYE BYE ***\n")


def exit_program(reason):
    LOG.error(reason)
    LOG.error("Exit Program!")
    print_bye()
    exit(1)


def get_rover_positions(cmd_invokers):
    output_txt = ""
    for rover_invoker in cmd_invokers:
        rover, invoker = rover_invoker
        invoker.execute_commands()
        LOG.info("Final rover position: {}".format(str(rover)))
        output_txt += "{} \n".format(str(rover))
    return output_txt


def main():
    args = parse_arguments()
    configure_logging(args.verbose)

    print_welcome()
    check_input_file(args.input_file)

    c = CommandParser(args.input_file)
    try:
        command_invokers = c.parse()
        rover_positions_str = get_rover_positions(command_invokers)
        write_output_file(args.output_file, rover_positions_str)
    except Exception as e:
        exit_program("Input file contains invalid input: {}".format(str(e)))

    print_bye()


if __name__ == "__main__":
    main()
