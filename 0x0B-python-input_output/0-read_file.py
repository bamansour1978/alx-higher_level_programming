#!/usr/bin/python3
# 0-read_file.py
"""A function that reading  file."""


def read_file(filename=""):
    """Print a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
