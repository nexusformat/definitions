from ..globals import directories
from ..utils.copy import copydir


def impatient_args(parser):
    parser.add_argument(
        "--prepare",
        action="store_true",
        help="Create the build files for the NeXus Impatient Guide",
    )


def impatient_exec(args):
    if args.prepare:
        copydir(directories.impatient_source_root(), directories.impatient_build_root())
