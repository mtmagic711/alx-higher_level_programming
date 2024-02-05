#!/usr/bin/python3
"""Define a class that inherirts from a list"""


class MyList(list):
    """class MyList"""

    def print_sorted(self):
        """A method that print the elements of the list sorted"""

        print(sorted(self))
