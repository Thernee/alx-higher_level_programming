#!/usr/bin/python3

""" A class that checks for instance of an object"""


def is_kind_of_class(obj, a_class):
    """Define the class"""
    if isinstance(obj, a_class):
        return True
    return False
