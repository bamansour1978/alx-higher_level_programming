#!/usr/bin/python3
"""1. Divide a matrix"""
def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix."""
    if (matrix == [] or matrix == [[]] or type(matrix) is not list or
        not all(type(row) is list for row in matrix)):
            raise TypeError("matrix must be a matrix (list of lists)"
                            "of integers/floats")
    
    for column in matrix:
            for ele in column:
                if type(ele) not in [int, float]:
                    raise TypeError("matrix must be a matrix (list of lists) "
                                    "of integers/floats")                         
            if len(column) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), column)) for column in matrix]