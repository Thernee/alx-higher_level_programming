#!/usr/bin/python3

"""Adds new attribute to object"""


def add_attribute(object, name, value):
    """ Define the add_attribute function"""

    if hasattr(object, "__dict__"):
        setattr(object, name, value)
    else:
        raise TypeError("can't add new attribute")
