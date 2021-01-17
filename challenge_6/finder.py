# Steps

# Create the class Find

# A method to list directory
# A method to filter files from a directory
# A method to execute command 

import os
import glob
import sys
from pathlib import Path

class Finder:
    """A Pythonic way of linux find command"""
    
    def __init__(self, args):
        self.args = args
        self.founded = list()
        self.start_path = Path(self.args.dir[0])

    def __check_dir(self):
        if os.path.exists(self.args.dir[0]):
            pass
        else:
            print("No such file or directory")
            sys.exit(1)

    def __find_by_name(self):
        
        filtered = self.start_path.rglob(self.args.name)
        
        self.founded.append(filtered)


    def __find_by_type(self):
        
        content = self.start_path.rglob(self.args.name or "*")

        if self.args.type == "d":
            filtered = [f for f in content if f.is_dir()]
        
        elif self.args.type =="f":
            filtered = [f for f in content if f.is_file()]

        else:
            print(f"Invalid type {self.args.type}. Supported types: 'd' and 'f'.")
            sys.exit(1)    
        
        self.founded.append(filtered)

    def __execute_cmd(self):
        for f in self.founded[0]:
            os.system(self.args.command.format(f))


    def find(self):
        self.__check_dir()

        if self.args.name and not self.args.type:
            self.__find_by_name()

        elif self.args.type:
            self.__find_by_type()

        else:
            print("You need either --name or --type")
            sys.exit(1)

        if self.args.command:
            self.__execute_cmd()

        if self.args.show:
            for f in self.founded[0]:
                print(f)
            
    

