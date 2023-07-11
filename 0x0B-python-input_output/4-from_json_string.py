#!/usr/bin/python3
# 4-from_json_string.py
""" A function that JSON-to-object"""
import json


def from_json_string(my_str):
    """Return to the representation of a JSON string."""
    return (json.loads(my_str))
