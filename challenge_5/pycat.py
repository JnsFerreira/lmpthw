from concat import Concat
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description= "Pythonic way of unix command called cat (concat)")

    # Positional Arguments for file(s)
    parser.add_argument("files", metavar="F", nargs="+",
                        help="A single or a list of files to be concatenated")

    # Output file flag
    parser.add_argument("-o", "--output",
                        help="The output file that will contain the concatenated files")

    args = parser.parse_args()

    cat = Concat()

    cat.concat(file_list=args.files, output_file= args.output)

if __name__ == '__main__':
    main()
