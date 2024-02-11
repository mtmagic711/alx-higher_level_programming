#!/usr/bin/python3
"""The class Rectangle that inherits from class Base."""
from models.base import Base


class Rectangle(Base):
    """The class Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self, y):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self, y):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
