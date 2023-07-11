#!/usr/bin/python3
# 5-save_to_json_file.py
"""A function writes a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a file txt using JSON """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
