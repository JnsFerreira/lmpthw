# Steps

# Create an argument to receive the file name
# Create an argument to print
# Create a positional argument to receive the diretory
# For last but not least, an argument to exec a command to file

from finder import Finder
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="A pythonic way of linux find command")

    parser.add_argument("dir", metavar="D",
                        help="Directory to search files")

    parser.add_argument("-n", "--name", 
                        help="Filter files by name")
    
    
    parser.add_argument("-p", "--print", action='store_true',
                        help="If used, print all founded files")
    
    parser.add_argument("-e", "--exec",
                        help="Receive a command and execute on all founded files")

    args = parser.parse_args()

    find = Finder(args=args)

    find.find()


if __name__ == '__main__':
    main()
