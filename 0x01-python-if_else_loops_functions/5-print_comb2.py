#!/usr/bin/python3
for Num in range(0, 100):
    if Num == 99:
        print("{}".format(Num))
    else:
        print("{:02}".format(Num), end=", ")
