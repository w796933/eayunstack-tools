import pkg_resources


def make_subcommand(parser, command):
    subp = parser.add_subparsers(
        title='Commands',
        metavar='COMMAND',
        help='DESCRIPTION',
        )

    entry_points = [
        (e.name, e.load())
        for e in pkg_resources.iter_entry_points(command + '_command')
    ]
    for (name, fn) in entry_points:
        p = subp.add_parser(
            name,
            description=fn.__doc__,
            help=fn.__doc__,
        )
        fn(p)
    return parser