#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for index in range(x):
        try:
            value = my_list[index]
            print(value, end="")
            count += 1
        except IndexError:
            print()
    print()
    return count
