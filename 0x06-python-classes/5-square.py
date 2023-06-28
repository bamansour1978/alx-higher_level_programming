#!/usr/bin/python3
# 4-square.py
# BAMANSOUR Abdennebi
"""A class Square that defines a square."""


class Square:
    """A square"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The new square's size.
        """
        self.size = size

    @property
    def size(self):
        """Size of the square"""
        return self._Square__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        """Return the area of the square"""
        return self.size * self.size

    def my_print(self):
        for index in range(0, self.__size):
            {print("#", end="") for jndex in range(self.__size)}
            print("")
        if self.__size == 0:
            print("")
