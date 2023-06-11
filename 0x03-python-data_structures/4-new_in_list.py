#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    if my_list:
        new_copy = my_list.copy()
        if idx < 0:
            return new_copy
        elif idx >= len(my_list):
            return new_copy
        else:
            new_copy[idx] = element
            return new_copy
