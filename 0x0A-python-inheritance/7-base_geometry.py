#!/usr/bin/python3
# 5-base_geometry.py
"""An empty class BaseGeometry."""


class BaseGeometry:
    """Represent base_geometry."""
    def area(self):
        """case : not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name : The name of the parameter.
            value : The parameter to validate.
        Raises:
            TypeError: If value != integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
