#!/usr/bin/python3
import random

try:
    number = random.randint(-10000, 10000)
    string = repr(number)
    n = int(string[-1])

    if n < 6 and n != 0 or number < 0:
        if number < 0:
            n = -n
        print("Last digit of {} is {} and is less than 6 and not 0\
        ".format(number, n))
    elif n > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, n))
    elif n == 0:
        print("Last digit of {} is {} and is 0".format(number, n))

except ValueError:
    print("TypeError")
