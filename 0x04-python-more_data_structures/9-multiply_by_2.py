#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    multiplied_dict = {}
    for key in a_dictionary.keys():
        holder = a_dictionary[key]
        multiplied_dict[key] = holder * 2

    return multiplied_dict
