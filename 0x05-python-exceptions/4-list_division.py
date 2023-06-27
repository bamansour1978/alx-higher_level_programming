#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list_ = [0] * list_length
    for index in range(list_length):
        try:
            res = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except TypeError:
            print("wrong type")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            list_.append(res)
    return (list_)
