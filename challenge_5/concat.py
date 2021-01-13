# Steps

# Create a class cat
# Write a function that can read text files
# Write a function that can show the content of a file
# Receive N files as arguments
# Identify if the -0 as passed as argument
# Write a function that can concat files

# TODO: Improve how to handle with invalid/nonexistent files

class Concat:
    """A Pythonic way of unix command cat"""

    def __read_file(self, file_name):
        """
        Description
            Reads text files
        
        Args
            file_name (String): The path of file to be read
        
        Returns
            data (String): The text file converted as string
        """
        try:
            f = open(file_name, 'r')
            data = f.read()
        
        except FileNotFoundError:
            print(f"{file_name} does not exist. Please, inform a valid path! Skipping file...")
            return None

        except Exception as e:
            print(f"Error while reading file. Details: {e}")
            return None
        
        return data

    def __show_content(self, data):
        """
        Description
            Just displays the content of a text file

        Args
            data(String): The text file that will be displayed
    
        Returns
            Nothing. Simply prints the content
        """
        print(data)

    def concat(self, file_list, output_file):
        """
        Description
            If specified a output file, displays the content and creates a output file concatenated. 
            Otherwise, just displays the content

        Args
            file_list (List): A list of files path to be read
            output_file (String): If specified, create this text file with concatenated files from file_list

        Returns
            Nothing.
        """
        if(output_file):
            with open(output_file, 'w') as outfile:        
                for file_name in file_list:
                    data = self.__read_file(file_name)
                    
                    if(data):
                        self.__show_content(data)
                        outfile.write(data)

        else:
            for file_name in file_list:
                data = self.__read_file(file_name)
                
                if(data):
                    self.__show_content(data)
