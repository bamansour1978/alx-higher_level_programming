#!/usr/bin/python3
# 1-square.py
# BAMANSOUR Abdennebi
"""class Square that defines a square by: (based on 0-square.py"""


class Square(object):
    """ A square """

    def __init__(self, size):
        """Init a new square
        Args: size (int): new square's size
        """
        self.__size = size
