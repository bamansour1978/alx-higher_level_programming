#!/usr/bin/python3
# 9-rectangle.py
"""A class Rectangle that inherit from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represente a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new rectangle.

        Args:
            width : The width (int).
            height : The height (int).
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """The area rectangle."""
        return (self.__width * self.__height)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)