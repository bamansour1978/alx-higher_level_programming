#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    a = new_list
    b = len(new_list)
    return [a[i] if a[i] != search else replace for i in range(b)]
