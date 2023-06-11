#!/usr/bin/python3

def max_integer(my_list=[]):

    if not my_list:
        return None

    maxx = 0
    for num in my_list:
        if num > maxx:
            maxx = num

    return maxx
