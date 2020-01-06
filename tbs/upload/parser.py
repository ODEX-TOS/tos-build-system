import argparse

COMMAND="upload"

def commands(subparser):
    """
    Returns a subparser with the given commands for the dependencies
    """
    parser = subparser.add_parser(COMMAND)

    parser.add_argument('--repo', '-r', help='Upload the repository. Be awair that uncomplete repositories will override existing packages. Only upload full repositories', action='store_true')
    parser.add_argument('--image', '-i', help='Upload all images', action='store_true')
    parser.add_argument('--all', '-a', help='Upload everything', action='store_true')

