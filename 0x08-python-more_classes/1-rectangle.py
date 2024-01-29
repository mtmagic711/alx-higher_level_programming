#!/usr/bin/python3
"""Define a class rectangle"""


class Rectangle():
    """the class rectangle"""
    def __init__(self, width=0, heigth=0) -> None:
        self.width = width
        self.heigth = heigth

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def heigth(self):
        return self.__heigth

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
