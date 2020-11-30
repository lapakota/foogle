import sys

from args_parser import ArgsParser
from reverse_index import ReverseIndex


def main():
    args = ArgsParser.parse_args(sys.argv[1:])
    directory = args.directory
    index = ReverseIndex(directory)
    print(index.make_reverse_index())


if __name__ == '__main__':
    main()

