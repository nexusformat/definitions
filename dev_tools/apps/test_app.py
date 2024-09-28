from pathlib import Path

from ..nxdl import iter_definitions
from ..nxdl import validate_definition


def nxtest_args(parser):

    pass


def nxtest_exec(args):
    print(args.source_root)
    for path in iter_definitions(Path(args.source_root)):
        print(path, end="", flush=False)
        validate_definition(path)
        print(" [passed]")
