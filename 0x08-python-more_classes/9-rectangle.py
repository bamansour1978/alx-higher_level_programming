#!/usr/bin/python3
# 8-rectangle.py
""" A rectangle class"""


class Rectangle:
    """ A rectangle representation

    attributes:
        number_of_istances : number of instance's rectangle
        print_symbol = "#"
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize a rectangle
        args:
            - `width`: the length of one side (int > 0).
            - `height`: the other side's length (int > 0).
        """

        type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns greater rectangle area

        args:
            rect_1 : first rectangle to compare
            rect_2 : second rectangle to compare
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ Create and returns new Square class based on given side length."""
        return cls(size, size)

    def __str__(self):
        """ Return string with information about this object #"""
        if self.__height * self.__width == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            [rectangle.append(str(self.print_symbol)) for
                j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """ A string representation of the rectangle"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        """ message before deletion of a rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
