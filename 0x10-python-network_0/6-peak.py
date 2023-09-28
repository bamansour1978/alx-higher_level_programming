#!/usr/bin/python3
"""peak-finding algorithm"""

def find_peak(list_of_integers):
    """
    Return a peak in a list of unsorted integers using a recursive binary search.
    """

    # Check if the list is empty
    if not list_of_integers:
        return None

    # Get the middle index of the list
    mid = len(list_of_integers) // 2

    # Check if the middle element is a peak
    if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
       (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
        return list_of_integers[mid]

    # If the middle element is not a peak, recurse on the side with a larger neighboring element
    if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])

