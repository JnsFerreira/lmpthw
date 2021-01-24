from argparse import ArgumentParser
from grepy import Grep

def parse_args():
    parser = ArgumentParser(description="Global Regular Expression Print")

    parser.add_argument("pattern", type=str, nargs=1, 
                        help="A Regex expression")

    parser.add_argument("directory", type=str, nargs=1,
                        help="Directory to search for patterns into files")

    parser.add_argument("-r", "--recursive", action="store_true",
                        help="")

    return parser.parse_args()


def main():
    
    args = parse_args()

    grep = Grep()

    grep.search(pattern = args.pattern[0], directory = args.directory[0])

if __name__ == '__main__':
    main()
