#!/usr/bin/python3
"""A class square that inherits from rectangle"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """The class square."""

    def __init__(self, size, x=0, y=0, id=None):
        """the constructor"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
