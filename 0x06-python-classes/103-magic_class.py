#!/usr/bin/python3

"""Define a MagicClass matching exactly a bytecode provided by ALX"""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initializes the Magic Class.
        Arg:
            radius (float or int): The radius of the Class.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the Magic Class."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns The circumference of the Magic Class."""
        return (2 * math.pi * self.__radius)
