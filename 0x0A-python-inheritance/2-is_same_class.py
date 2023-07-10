#!/usr/bin/python3
# 2-is_same_class.py
"""A class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj : The object .
        a_class : The class to match the type of object.
    Returns:
        True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return (True)
    return (False)
