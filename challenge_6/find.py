# Steps

# Create an argument to receive the file name
# Create an argument to print
# Create a positional argument to receive the diretory
# For last but not least, an argument to exec a command to file

from finder import Finder
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="A pythonic way of linux find command")

    parser.add_argument("dir", type=str, nargs=1,
                        help="Directory to search files")

    parser.add_argument("-n", "--name", type=str,
                        help="Filter files by name")
    
    parser.add_argument("-t", "--type", type=str,
                        help="filter files by type")
    
    parser.add_argument("-s", "--show", action='store_true',
                        help="If used, print all founded files")
    
    parser.add_argument("-cmd", "--command", type=str,
                        help="Receive a command and execute on all founded files")

    args = parser.parse_args()

    find = Finder(args=args)

    find.find()


if __name__ == '__main__':
    main()
