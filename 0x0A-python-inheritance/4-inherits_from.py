#!/usr/bin/python3
# 4-inherits_from.py
""" class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj: The object.
        a_class : The class to match the type of object.
    Returns:
        True.
        Or False.
    """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return (True)
    return (False)
