#!/usr/bin/python3

def max_integer(my_list=[]):

    if my_list == []:
        return None

    maxx = 0
    for num in my_list:
        if num > maxx:
            maxx = num

    return maxx



my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
