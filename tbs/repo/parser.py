import argparse

COMMAND="repo"

def commands(subparser):
    """
    Returns a subparser with the given commands for the dependencies
    """
    parser = subparser.add_parser(COMMAND)

    parser.add_argument('--packages', '-p', help='Build all basic packages', action='store_true')
    parser.add_argument('--fonts', '-f', help='Build all basic fonts', action='store_true')
    parser.add_argument('--kernel', '-k', help='Build the kernel using auto settings', action='store_true')
    parser.add_argument('--list', '-l', help='List all packages to generate', action='store_true')
    parser.add_argument('--list-fonts', '-lf', help='List all fonts that will be build', action='store_true')
    parser.add_argument('--list-packages', '-lp', help='List all packages that will be build', action='store_true')
    parser.add_argument('--sync', '-s', help='Sync all exisiting repo packages with the repo database', action='store_true')
    parser.add_argument('--all', '-a', help='Generate a full repository', action='store_true')

