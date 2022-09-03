from pathlib import Path
from argparse import ArgumentParser

from commands import init, build, serve


def parseargs():
    parser = ArgumentParser() 
    subparser = parser.add_subparsers()

    # init cmd parser
    initializer = subparser.add_parser('init', help='Initialize a lit project')
    initializer.add_argument('folder', nargs='?', type=Path, help='Path to folder to initalize project in')
    initializer.add_argument('-t', '--type', type=str, choices=['static', 'spa'], default='static', help='Lit projects can either be a static site, or a single page app') 
    initializer.set_defaults(func=init)

    # build cmd parser
    builder = subparser.add_parser('build', help='Parse entries into HTML')
    builder.set_defaults(func=build)

    # serve cmd parser
    server = subparser.add_parser('serve', help='Test website locally on dev server - reload server ')
    server.set_defaults(func=serve)
    return vars(parser.parse_args())


if __name__ == '__main__':
    kwargs = parseargs()
    cmd = kwargs.pop('func')
    cmd(**kwargs)
