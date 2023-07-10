#!/usr/bin/python3
# 0-lookup.py
"""Define an object attribute of lookup function."""


def lookup(obj):
    """ A function return a list of an object's available attributes."""
    return dir(obj)
