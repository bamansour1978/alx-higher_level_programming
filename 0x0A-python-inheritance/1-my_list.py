#!/usr/bin/python3
# 1-my_list.py
"""Defines an inherited of  list class My_List."""


class MyList(list):
    """ A class MyList that inherits from list:"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
