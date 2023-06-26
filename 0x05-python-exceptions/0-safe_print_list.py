#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for valor in my_list[:x]:
        try:
            print("{}".format(valor), end="")
            count += 1
        except IndexError as error:
           print()
    print()
    return count
