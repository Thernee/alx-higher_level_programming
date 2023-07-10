#!/usr/bin/python3

""" A class that checks for instance of an object"""


def is_same_class(obj, a_class):
    """Define the class"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
