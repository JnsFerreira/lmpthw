# Steps

# Show help with --help or -h
# Three or more arguments that are flags, meaning they turn on or off something
# Three or more arguments that are options, meaning they do take an argument and set a variable 
# Additional "positional" arguments wich are kust of files.


from argparse import ArgumentParser

parser = ArgumentParser(description = "Challenge 4")

# Options
parser.add_argument("Numbers", metavar='N', type=int, nargs='+')

# Flags
parser.add_argument("-fg1", "--flag1", action='store_true', help="Help for flag1")
parser.add_argument("-fg2", "--flag2", action='store_true', help="Help for flag2")
parser.add_argument("-fg3", "--flag3", action='store_true', help="Help for flag3")

# Positional
parser.add_argument("-p1", "--position1", help="Help for pos1")
parser.add_argument("-p2", "--position2", help="Help for pos2")
parser.add_argument("-p3", "--position3", help="Help for pos3")

# Parsing arguments
args = parser.parse_args()

print(args)
