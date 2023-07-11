#!/usr/bin/python3
# 6-load_from_json_file.py
"""A function that reading a JSON file."""
import json


def load_from_json_file(filename):
    """A JSON file -> Python object."""
    with open(filename) as file:
        return json.load(file)
