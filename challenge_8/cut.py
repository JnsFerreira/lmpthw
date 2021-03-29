from argparse import ArgumentParser
from cutpy import Cut


def parse_args():
    parser = ArgumentParser(description="")

    parser.add_argument(
        "input", type=str, nargs=1, help="A text input")

    parser.add_argument(
        "-d", "--delimiter", type=str, default=' ', help="Type of delimiter")

    parser.add_argument(
        "-f", "--fields", help="List of fields to extract, starting from 0.")

    return parser.parse_args()


def main():

    parsed_args = parse_args()

    cut_obj = Cut(args=parsed_args)

    output = cut_obj.cut()

    print(output)

if __name__ == '__main__':
    main()
