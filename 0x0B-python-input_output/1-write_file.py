#!/usr/bin/python3
# 1-write_file.py
"""A function that writing a file."""


def write_file(filename="", text=""):
    """Write a txt (string) to a UTF8 file.

    Args:
        filename : The file's name  to write (str).
        text : The text to write in file (str).
    Return:
        Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
