class Cut:
    def __init__(self, args):
        self.input = args['input']
        self.delimiter = args['delimiter']
        self.fields = args['fields']

    def _parse_input(self):
        if isinstance(self.input, str):
            return True

        else:
            raise TypeError("Input must be a string type") 

    def _split_by_delimiter(self):

        if self.delimiter == ' ':
            splited_text = self.input.split()
        else:
            splited_text = self.input.split(self.delimiter)

        if isinstance(splited_text, list):
            return splited_text

        else:
            raise TypeError(f"Could not splited input with delimiter {self.delimiter}")

    def _filter(self, splited_text: list):
        start_idx, end_idx  = self.fields.split("-")

        try:
            filtered_text = splited_text[int(start_idx):int(end_idx)]

        except IndexError as e:
            raise e

        return filtered_text

    def _generate_output(self, filtered_text):
        output = ''
        for text in filtered_text:
            output += f" {text}"

        return output
    
    def cut(self):
        self._parse_input()

        splited_text = self._split_by_delimiter()

        filtered_text = self._filter(splited_text=splited_text)

        output = self._generate_output(filtered_text=filtered_text)

        return output
