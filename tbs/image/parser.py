import argparse

COMMAND="image"

def commands(subparser):
    """
    Returns a subparser with the given commands for the images
    """
    parser = subparser.add_parser(COMMAND)

    parser.add_argument('--awesome', '-a', help='Build the tos awesome image', action='store_true')
    parser.add_argument('--server', '-s', help='Build the tos server image', action='store_true')
    parser.add_argument('--azerty', '-az', help='Build the current image with azerty as the default keybinding', action='store_true')
    parser.add_argument('--qwerty', '-q', help='Set the build image to the qwerty layout (default)', action='store_true')
    parser.add_argument('--suite', '-su', help='Build all images with a given keybinding', action='store_true')
    parser.add_argument('--all', help='Build all editions of tos with all keybindings', action='store_true')

    

