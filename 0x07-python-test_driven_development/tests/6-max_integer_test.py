#!/usr/bin/python3
# 6-max_integer_test.py
"""Unittests for max_integer ([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer for list"""

    def test_ordered_list(self):
        """Test list ordre of integers."""
        ordered = [5, 6, 7, 8]
        self.assertEqual(max_integer(ordered), 8)

    def test_unordered_list(self):
        """Test list unordered of integers."""
        unordered = [1, 9, 4, 3]
        self.assertEqual(max_integer(unordered), 9)

    def test_max_at_begginning(self):
        """Test a list with a beginning ."""
        max_at_beginning = [11, 10, 9, 8]
        self.assertEqual(max_integer(max_at_beginning), 11)

    def test_empty_list(self):
        """Test for an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a single element."""
        one_element = [79]
        self.assertEqual(max_integer(one_element), 79)

    def test_floats(self):
        """Test a list of floats numbers."""
        floats = [4.33, 6.33, -9.123, 15.3, 9.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 65.7, -1, 19, 60]
        self.assertEqual(max_integer(ints_and_floats), 65.7)

    def test_string(self):
        """Test for a string."""
        string = "Bamansour"
        self.assertEqual(max_integer(string), 'u')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Bren", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
