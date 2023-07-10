#!/usr/bin/python3

""" A class that checks for a subclass"""


def inherits_from(obj, a_class):
    """Define the class"""
    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    return False
