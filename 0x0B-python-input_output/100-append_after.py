#!/usr/bin/python3
# 100-append_after.py
"""A text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line in file txt.

    Args:
        filename : (str)
        search_string : (str)
        new_string : (str)
    """
    txt = ""
    with open(filename) as red:
        for line in red:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as wr:
        wr.write(txt)
