#!/usr/bin/python3
# 101-locked_class.py
""" A class """


class LockedClass:
    """
    prevents the user from dynamically creating new instance attributes
    """

    __slots__ = ["first_name"]
