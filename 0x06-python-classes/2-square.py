#!/usr/bin/python3
# 2-square.py
# BAMANSOUR Abdennebi
"""a class Square that defines a square by: (based on 1-square.py)"""


class Square(object):
    """A square"""

    def __init__(self, size=0):
        """Init a new Square.

        Args:
            size (int): The new square's size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
