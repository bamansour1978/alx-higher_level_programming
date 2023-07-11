#!/usr/bin/python3
# 3-to_json_string.py
"""A function string-to-JSON."""
import json


def to_json_string(my_obj):
    """Return : string ->JSON representation """
    return (json.dumps(my_obj))
