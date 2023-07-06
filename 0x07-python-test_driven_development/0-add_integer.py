#!/usr/bin/python3
# 0-add_integer.py
"""A function that adds 2 integers."""


def add_integer(a, b=98):
    """ Return integer
    args:
    a : first number to sum up with default value of '89'
    b : second number to sum up
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, (int, float)))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
