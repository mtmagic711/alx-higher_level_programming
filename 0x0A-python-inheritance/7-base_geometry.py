#!/usr/bin/python3
"""Defining a new class"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """Raises an Exception."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the argument value."""

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
