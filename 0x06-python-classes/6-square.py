#!/usr/bin/python3
# 6-square.py
# BAMANSOUR Abdennebi
"""A class Square that defines a square."""


class Square:
    """A square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The new square's size.
            position (int, int): new square's position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size of the square"""
        return (self.__size)

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, size):
        if (not isinstance(size, tuple) or
                len(size) != 2 or
                not all(isinstance(num, int) for num in size) or
                not all(num >= 0 for num in size)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = size

    def area(self):
        """Return the area of the square"""
        return self.size * self.size

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
