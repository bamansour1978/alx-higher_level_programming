#!/usr/bin/python3
# 10-square.py
""" A Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square's repr."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size : new square's size (int).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
