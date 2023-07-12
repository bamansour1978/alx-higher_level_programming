#!/usr/bin/python3
# 10-student.py
"""A class Student."""


class Student:
    """A student representation."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new_Student.

        Args:
            first_name : The first name of a student (str).
            last_name : The last name of a student (str).
            age : The age of the student (str).
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a Student's dictionary representation."""
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {ky: getattr(self, ky) for ky in attrs if hasattr(self, ky)}
        return (self.__dict__)
