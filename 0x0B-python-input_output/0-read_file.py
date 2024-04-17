#!/usr/bin/python3

def read_file(filename=""):
        """number of lines from file
    args:
        filename: file to read
    return:
        number of lines
    """
    with open(filename, encoding="utf-8") as f:
        for line in f.read():
            print(line, end="")
