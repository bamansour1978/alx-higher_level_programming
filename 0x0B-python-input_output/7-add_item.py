#!/usr/bin/python3
# 7-add_item.py
"""Added all args to a Python list and save them in a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items_p = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items_p = []
    items_p.extend(sys.argv[1:])
    save_to_json_file(items_p, "add_item.json")
