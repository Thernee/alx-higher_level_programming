#!/usr/bin/python3

""" A class that checks for instance of an object"""


def is_same_class(obj, a_class):
    """Define the class"""
    if type(obj) != a_class:
        return False
    return True
