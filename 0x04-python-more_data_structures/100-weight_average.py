#!/usr/bin/python3

def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    a = 0
    s = 0
    for tupl in my_list:
        a += (tupl[0] * tupl[1])
        s += tupl[1]
    return (a / s)
