import re
import os
from pathlib import Path

class Grep:

    def __read_file(self, file_name):
        try:
            lines = open(file_name).readlines()
        except UnicodeDecodeError:
            print(f"Binary file {file_name} matches.")
            
            return lines

    def __find_in_file(self, lines, pattern):
        exp = re.compile(pattern)

        for line in lines:
            if exp.search(line):
                print(line)

    def search(self, pattern, directory):
        start_path = Path(directory)

        for f in start_path.rglob("*"):
            if f.is_file():
                lines = self.__read_file(file_name = f)

                self.__find_in_file(lines=lines, pattern=pattern)