# FIND

Find search for files or directories based on starting directory and options setted on 
 
# Installation


1. Clone the repository

```
$ git clone https://github.com/JnsFerreira/lmpthw.git
```

2. Go to `challenge_6` folder

```
$ cd lmpthw/challenge_6
```

3. Execute the `find.py` file

```
$ python3 find.py [OPTIONS]
```
# Basic usage

```
$ python3 find.py [STARTING_DIRECTORY] [NAME] [TYPE] [COMMAND] [SHOW]
```

- `starting_directory`: The initial directory to search 
- `-n` or `--name`: File name to be seach
- `-t` or `--type`: Type to be search. Can be "f" for files or "d" to directories
- `-cmd` or `--command`: For founded files or directories, apply the command. You must pass a string with this format: `<command> {}`. The file or directory name will be replaced on {}
- `-s` or `--show`: Display the results.

**Example:** Find all text files and show the content with cat command, starting at foo/bar directory

```
$ python3 find.py "foo/bar/" --name "*.txt" --type "f" --command "cat {}" --show
```

