#!/usr/bin/python3

""" A definition of BaseGeometry class"""


class BaseGeometry():
    """ Define BaseGeometry class"""
    pass

    def area(self):
        """ return area of a geometry shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ comfirms value type"""
        if type(value)  is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
