import argparse

COMMAND="kernel"

def commands(subparser):
    """
    Returns a subparser with the given commands for the kernel
    """
    parser = subparser.add_parser(COMMAND)

    parser.add_argument('--build', '-b', help='Build the latest kernel version', action='store_true')
    parser.add_argument('--cores', '-c', help='Specify howmany cores to use', type=int, default=1)
    parser.add_argument('--auto', '-a', help='Auto detect howmany cores to use', action='store_true')

