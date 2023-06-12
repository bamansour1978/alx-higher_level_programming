#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in (row):
            if row[len(row) - 1] == column:
                print("{:d}".format(column), end="")
            else:
                print("{:d}".format(column), end=" ")
        print("".format())
