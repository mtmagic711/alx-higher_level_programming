#!/usr/bin/python3
"""Define a function that returns the list
of available attributes and methods of an object"""


def lookup(obj):
    """It takes an object and return a list"""

    return dir(obj)
