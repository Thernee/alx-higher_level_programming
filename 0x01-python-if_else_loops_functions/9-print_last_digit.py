#!/usr/bin/python3

def print_last_digit(number):

    string = repr(number)

    n = int(string[-1])
    print(n, end="")
    return n
