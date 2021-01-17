# Steps

# Create the class Find

# A method to list directory
# A method to filter files from a directory
# A method to execute command 

import os
import glob

class Finder:
    """A Pythonic way of linux find command"""
    
    def __init__(self, args):
        self.files = list()
        self.args = args


    def __list_directory(self, path):
        if(os.path.exists(path)):
            self.files.append(os.listdir(path))
        
        else:
           print("No such file or directory")

    def __filter_files(self, condition):
        return glob.glob(condition)    
            
    def __show_files(self):
        for f in self.files:
            print(f)

    def find(self):
        print(self.args.dir)
