#!/usr/bin/python3

"""
Define say_my_name function
Takes 2 arguments (first_name and last_name)
Returns: fullname if successful, raises error otherwise
"""


def say_my_name(first_name, last_name=""):
    """
    print name passed
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
