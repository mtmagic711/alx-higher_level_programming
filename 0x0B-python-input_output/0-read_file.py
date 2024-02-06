#!/usr/bin/python3
"""A function that open a file"""


def read_file(filename=""):
    """the read file function """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
