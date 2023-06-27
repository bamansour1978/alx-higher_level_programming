#!/usr/bin/python3
# 4-square.py
# BAMANSOUR Abdennebi
"""a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """A square"""

    def __init__(self, size=0):
        """Init a new Square.

        Args:
            size (int): The new square's size.
        """
        self.size = size

        @property
        def size(self):
            """ size of squre"""
            return (self._Square__size)

        @size.setter
        def size(self, size):
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self._Square__size = size

    def area(self):
        """ function return area of the square"""
        return (self.size * self.size)
