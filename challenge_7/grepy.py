import re
import os
from pathlib import Path

class Grep:
    def __read_file(self, file_name):
        try:
            lines = open(file_name).readlines()
        except UnicodeDecodeError:
            #print(f"Binary file {file_name} matches.")
            return ""
            
        return lines

    def __find_in_file(self, lines, pattern):
        try:
            exp = re.compile(pattern)

        except Exception as e:
            print(f"Invalid Regular Expression")
            raise e

        for line in lines:
            if exp.search(line):
                print(line)

    def search(self, pattern, location, recursive=False):
        path = Path(location)

        if recursive:
            for f in start_path.rglob("*"):
                if f.is_file():
                    lines = self.__read_file(file_name = f)
                    self.__find_in_file(lines=lines, pattern=pattern)
        
        else:
            if path.is_file():
                lines = self.__read_file(file_name = location)
                self.__find_in_file(lines=lines, pattern=pattern)
            else:
                print("You need to specify a file name or --recursive to seach in all files in a directory")