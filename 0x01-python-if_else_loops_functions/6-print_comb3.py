#!/usr/bin/python3
for Num1 in range(0, 10):
    for Num2 in range(Num1 + 1, 10):
        if Num2 == 9 and Num1 == 8:
            print("{}{}".format(Num1, Num2))
        else:
            print("{}{}".format(Num1, Num2), end=", ")
