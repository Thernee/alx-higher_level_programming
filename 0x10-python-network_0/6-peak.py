#!/usr/bin/python3

""" Module Doc. for find_peak()"""


def find_peak(list_of_integers):
    """find the peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    else:
        temp_list = list(list_of_integers)
        temp_list.sort()
        return temp_list[-1]
