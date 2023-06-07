#!/usr/bin/python3
def fizzbuzz():
    for Num in range(1, 101):
        if Num % 3 == 0 and Num % 5 == 0:
            print("FizzBuzz ", end="")
        elif Num % 3 == 0:
            print("Fizz ", end="")
        elif Num % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(Num), end="")
