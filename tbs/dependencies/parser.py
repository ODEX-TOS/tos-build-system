import argparse

COMMAND="dependency"

def commands(subparser):
    """
    Returns a subparser with the given commands for the dependencies
    """
    parser = subparser.add_parser(COMMAND)

    parser.add_argument('--repo', '-r', help='Install all repo dependencies', action='store_true')
    parser.add_argument('--image', '-i', help='Install all tos image dependencies', action='store_true')
    parser.add_argument('--kernel', '-k', help='Install all kernel dependencies', action='store_true')
    parser.add_argument('--upload', '-u', help='Install all data upload dependencies', action='store_true')
    parser.add_argument('--repo-full', '-rf', help='Install a full repo dependencies (includes --repo and --kernel)', action='store_true')
    parser.add_argument('--all', '-a', help='Install all dependencies', action='store_true')

