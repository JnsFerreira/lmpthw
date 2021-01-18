# CONCAT

A Pythonic way of cat unix command. Basically, you can use concat by two ways: 

1. See the content of a file

2. Concatenate N files, being able to write to an output file

## Installation

1. Clone the repository

```
$ git clone https://github.com/JnsFerreira/lmpthw.git
```

2. Go to `challenge_5` directory

```
$ cd lmpthw/challenge_5
```

3. Execute the `pycat.py` file

```
$ python3 pycat.py [OPTIONS]
```

## Basic Usage

```
$ python3 pycat.py [FILES] [OUTPUT]
```

- `files`: A single or a list of files to be concatenated
- `output`: The output file that will contain the concatenated files

**Example:**: Concatenate the file1.txt, file2.txt and file3.txt located at input_files folder. Write the result to output_files/output.txt

```
$ python3 pycat.py input_files/file1.txt input_files/file2.txt input_files/file3.txt -o output_files/output.txt
```

**Tip**: I've already created 3 input files, so you can easily test pycat.
