#!/usr/bin/python3
"""A function that write in a file"""


def write_file(filename="", text=""):
    """A function that takes a filename and a text"""

    with open(filename, 'w', encoding='UTF-8') as f:
        return f.write(text)
