#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    from sys import argv

    if len(argv) != 4:
        print("Usage: {} <a> <opeartor> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))

    elif argv[2] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))

    elif argv[2] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))

    elif argv[2] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))

    else:
        print("Unknown opeartor. Available opeartors: +, -, * and /")
        exit(1)
