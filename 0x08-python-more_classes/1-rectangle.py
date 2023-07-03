#!/usr/bin/python3
# 1-rectangle.py


class Rectangle:

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    @property
    def width(self):
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
        return self.__height

    @height.setter
    def height(self, valor):
        if not isinstance(valor, int):
            raise TypeError("height must be an integer")
        if valor < 0:
            raise ValueError("height must be >= 0")
        self.__height = valor
