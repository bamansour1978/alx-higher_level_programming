#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        r = add(a, b)
        for j in range(4,6):
            r = add(r, j)
        return (r)
    else:
        return(sub(a, b))