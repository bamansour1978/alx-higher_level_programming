#!/usr/bin/python3
# 4-append_write.py
"""A function that append a file."""


def append_write(filename="", text=""):
    """Appends a str to the end of a UTF8 file txt.

    Args:
        filename : The name of the file to append to (str).
        text : The string to append in the file (str).
    Return:
        The number of characters append to file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return (file.write(text))
