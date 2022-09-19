from ..globals import directories


def dir_args(parser):
    parser.add_argument(
        "--source-root",
        type=str,
        default=None,
        help="Source root directory" f" Default: {directories.get_source_root()}",
    )
    parser.add_argument(
        "--nxdl-root",
        type=str,
        default=None,
        help="NXDL root directory" f" Default: {directories.get_nxdl_root()}",
    )
    parser.add_argument(
        "--build-root",
        type=str,
        default=None,
        help="Build root directory" f" Default: {directories.get_build_root()}",
    )


def dir_exec(args):
    if args.source_root:
        directories.set_source_root(args.source_root)
    if args.nxdl_root:
        directories.set_nxdl_root(args.nxdl_root)
    if args.build_root:
        directories.set_build_root(args.build_root)
