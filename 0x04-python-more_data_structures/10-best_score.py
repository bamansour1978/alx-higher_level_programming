#!/usr/bin/python3
def best_score(a_dictionary):
    """a function that Returns a key with the
    biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    r = list(a_dictionary.keys())[0]
    b = a_dictionary[r]
    for key, value in a_dictionary.items():
        if value > b:
            b = value
            r = key
    return (r)
