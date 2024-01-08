#!/usr/bin/python3
"""defines a class called Mylist"""


class Mylist(list):
    """A class that inherits from a list"""

    def print_sorted(self):
        """A method that print a sorted list"""
        print(sorted(self))
