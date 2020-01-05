import argparse

COMMAND="launcher"

def commands(subparser):
    """
    Returns a subparser with the given commands for the dependencies
    """
    parser = subparser.add_parser(COMMAND)

    parser.add_argument('--repo-full', '-rf', help='Build a full repository including kernel and upload it', action='store_true')
    parser.add_argument('--repo', '-r', help='Build a repo and upload it', action='store_true')
    parser.add_argument('--kernel', '-k', help='Build all images and upload it', action='store_true')
    parser.add_argument('--all', '-a', help='Build everything and upload it', action='store_true')

