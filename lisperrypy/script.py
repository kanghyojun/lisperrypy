import sys

from argparse import ArgumentParser, FileType

from . import program

def main():
    parser = ArgumentParser(description='Run lisperrypy!')
    parser.add_argument('--repl', '-r',
                        help='Running REPL', action='store_true')
    parser.add_argument('file', nargs='?', type=FileType('r'),
                        help='*.lpy file')
    args = parser.parse_args()
    if args.repl or (not args.repl and args.file is None):
        while True:
            code = input("> ")
            if code == '':
                pass
            else:
                try:
                    print(program(code))
                except KeyboardInterrupt:
                    sys.exit(0)
        readline.redisplay()
    elif args.file is not None:
        program(args.file.read())

