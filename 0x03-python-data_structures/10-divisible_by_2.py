#!/bin/python3

def divisible_by_2(my_list=[]):
    if my_list:
        new_list = []
        # new_list = [True if num % 2 == 0 else False for num in my_list]
        for num in my_list:
            if num % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
        return new_list
