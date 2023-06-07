#!/usr/bin/python3

j = 0
for s in range(ord('z'), ord('a') -1, -1):
    print("{}".format(chr(s - j)), end="")
    j = 32 if j == 0 else 0
