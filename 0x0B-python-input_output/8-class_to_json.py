#!/usr/bin/python3
# 10-class_to_json.py
"""A function Python class-to-JSON."""


def class_to_json(obj):
    """Return to dictionary represntation of simple data ."""
    return obj.__dict__
