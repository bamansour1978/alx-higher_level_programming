#!/usr/bin/python3
# 12-pascal_triangle.py
"""A Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    """
    if n <= 0:
        return []

    triangl = [[1]]
    while len(triangl) != n:
        tr = triangl[-1]
        temp = [1]
        for j in range(len(tr) - 1):
            temp.append(tr[j] + tr[j + 1])
        temp.append(1)
        triangl.append(temp)
    return (triangl)
