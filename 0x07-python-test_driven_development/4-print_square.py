#!/usr/bin/python3

"""
Define print_square function
Takes 1 argument (size)
Prints a square of size 'size' with # character
"""


def print_square(size):
    """
    prints square with the # character
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")

    if size == 0:
        print()
    else:
        for num in range(0, size):
            i = size
            while i > 0:
                print("#", end="")
                i -= 1
            print()
