#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string1 = " and is greater than 5"
string2 = " and is 0"
string3 = " and is less than 6 and not 0"
if number < 0:
    last_d = number % -10
else:
    last_d = number % 10
if last_d == 0:
    print("Last digit of {} is {}".format(number, last_d) + string2)
elif last_d > 5:
    print("Last digit of {} is {}".format(number, last_d) + string1)
else:
    print("Last digit of {} is {}".format(number, last_d) + string3)
    
