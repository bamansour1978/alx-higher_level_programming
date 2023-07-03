#!/usr/bin/python3
# 2-rectangle.py
""" A rectangle class"""


class Rectangle:
    """ A rectangle representation"""
    def __init__(self, width=0, height=0):
        """ Initialize a rectangle
        args:
            - `width`: the length of one side (int > 0).
            - `height`: the other side's length (int > 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, valor):
        if type(valor) is not int:
            raise TypeError("width must be an integer")
        if valor < 0:
            raise ValueError("width must be >= 0")
        self.__width = valor

    @property
    def height(self):
        """Get the heigth of a rectangle."""
        return self.__height

    @height.setter
    def height(self, valor):
        if not isinstance(valor, int):
            raise TypeError("height must be an integer")
        if valor < 0:
            raise ValueError("height must be >= 0")
        self.__height = valor

    def perimeter(self):
        """ a perimeter of the rectangle"""
        if self.__height * self.__width == 0:
            return 0
        return ((self.__height + self.__width) * 2)

    def area(self):
        """ The area of the rectangle"""
        return self.__height * self.__width
