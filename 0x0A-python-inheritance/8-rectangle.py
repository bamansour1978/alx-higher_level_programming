#!/usr/bin/python3
# 8-base_geometry.py
"""A rectangle class BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using base_geometry."""
    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width : The width of the new Rectangle.
            height : The height of the new Rectangle.
        """

        def __init__(self, width, height):
            """Intialize a new Rectangle.

            Args:
                width : The width of the new Rectangle.
                height: The height of the new Rectangle.
            """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
