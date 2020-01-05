import argparse

import tbs.dependencies.parser as deparser
import tbs.dependencies.main as demain

import tbs.image.parser as imparser
import tbs.image.main as immain

import tbs.kernel.parser as keparser
import tbs.kernel.main as kemain

import tbs.launcher.parser as laparser
import tbs.launcher.main as lamain

import tbs.repo.parser as reparser
import tbs.repo.main as remain

import tbs.upload.parser as upparser
import tbs.upload.main as upmain

# all subparsers must be added to this list
parsers = [
    deparser.commands,
    imparser.commands,
    keparser.commands,
    laparser.commands,
    reparser.commands,
    upparser.commands
]



parser = argparse.ArgumentParser(prog='tbs')
subparsers = parser.add_subparsers(dest='command')
for parse in parsers:
    parse(subparsers)

args = parser.parse_args()

if args.command == deparser.COMMAND:
    demain.main(args)
elif args.command == imparser.COMMAND:
    immain.main(args)
elif args.command == keparser.COMMAND:
    kemain.main(args)
elif args.command == laparser.COMMAND:
    lamain.main(args)
elif args.command == reparser.COMMAND:
    remain.main(args)
elif args.command == upparser.COMMAND:
    upmain.main(args)

