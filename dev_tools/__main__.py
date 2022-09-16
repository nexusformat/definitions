import argparse
import sys

from .apps import dir_app
from .apps import impatient_app
from .apps import manual_app
from .apps import nxclass_app


def main(argv=None):
    parser = argparse.ArgumentParser(description="NeXus development tools")

    subparsers = parser.add_subparsers(help="Commands", dest="command")

    nxclass_parser = subparsers.add_parser(
        "nxclass", help="Test and documentation for a single NeXus class"
    )
    nxclass_app.nxclass_args(nxclass_parser)
    dir_app.dir_args(nxclass_parser)

    manual_parser = subparsers.add_parser(
        "manual", help="Test and prepare User Manual building"
    )
    manual_app.manual_args(manual_parser)
    dir_app.dir_args(manual_parser)

    impatient_parser = subparsers.add_parser(
        "impatient", help="Prepare Impatient Guide building"
    )
    impatient_app.impatient_args(impatient_parser)
    dir_app.dir_args(impatient_parser)

    if argv is None:
        argv = sys.argv
    args = parser.parse_args(argv[1:])

    if args.command == "nxclass":
        dir_app.dir_exec(args)
        nxclass_app.nxclass_exec(args)
    elif args.command == "manual":
        dir_app.dir_exec(args)
        manual_app.manual_exec(args)
    elif args.command == "impatient":
        dir_app.dir_exec(args)
        impatient_app.impatient_exec(args)
    else:
        parser.print_help()
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
