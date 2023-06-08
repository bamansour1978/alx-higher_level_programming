#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    Num_arg = len(sys.argv) - 1
    if Num_arg == 0:
        print("0 arguments.")
    elif Num_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(Num_arg))
    for i in range(Num_arg):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
