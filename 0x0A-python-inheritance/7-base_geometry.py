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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
