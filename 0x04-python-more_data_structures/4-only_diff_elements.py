#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    holder = set_1 ^ set_2
    return sorted(holder)
