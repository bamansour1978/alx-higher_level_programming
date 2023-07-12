#!/usr/bin/python3
# 101-add_attribute.py
"""A function that add attr to obj."""


def add_attribute(obj, att, value):
    """Add a new attr to an obj if possible.

    Args:
        obj : The obj to add an attr to (any).
        att : The name of the attr to add to obj (str).
        value : The value of att (any)
    Raise:
        TypeError: If the attr can not be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
