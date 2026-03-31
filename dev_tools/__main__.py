import argparse
import sys

from .apps import dir_app
from .apps import impatient_app
from .apps import manual_app
from .apps import nxclass_app
from .apps import test_app


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

    nxtest_parser = subparsers.add_parser("nxtest", help="Test definition files")
    test_app.nxtest_args(nxtest_parser)
    dir_app.dir_args(nxtest_parser)

    if argv is None:
        argv = sys.argv
    args = parser.parse_args(argv[1:])

    app_exec = {
        "nxclass": nxclass_app.nxclass_exec,
        "manual": manual_app.manual_exec,
        "impatient": impatient_app.impatient_exec,
        "nxtest": test_app.nxtest_exec,
    }.get(args.command)

    if app_exec is None:
        parser.print_help()
        return 1

    dir_app.dir_exec(args)
    return 0 if not app_exec(args) else 1


if __name__ == "__main__":
    sys.exit(main())
