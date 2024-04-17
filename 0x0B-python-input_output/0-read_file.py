#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        for line in f.read():
            print(line, end="")
