# Steps

# Create a class cat
# Write a function that can read text files
# Write a function that can show the content of a file
# Receive N files as arguments
# Identify if the > as passed as argument
# Write a function that can concat files

# Libraries
from argparse import ArgumentParser

class Concat:
    def __init__(self):
        pass

    def read_file(self, file):
        pass

    def show_content(self, file):
        pass

    def concat(self, file_list, output_file):
        pass



def main():
    parser = ArgumentParser(description= "Pythonic way of unix command called cat (concat)")
    
    # Positional Arguments for file(s)
    parser.add_argument("files", metavar="F", nargs="+",
                        help="A single or a list of files to be concat")
    
    # Concat flag
    parser.add_argument("-o", "--output", 
                        help="The output file containing the concated files")

    args = parser.parse_args()
    
    cat = Concat()
    
    cat.concat(file_list=args.files, output_file= args.output)
    
if __name__ == '__main__':
    main()
