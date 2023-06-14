#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list:
        holder = set(my_list)
        result = 0

        for num in holder:
            result += num
        return result
