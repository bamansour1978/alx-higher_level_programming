#!/usr/bin/python3
# 100-my_int.py
"""A class MyInt that inherits from int."""


class MyInt(int):
    """Invert int op == and !="""

    def __eq__(self, value):
        """Override == opeartor without != behavior."""
        return (self.real != value)

    def __ne__(self, value):
        """Override != operator without == behavior."""
        return (self.real == value)
