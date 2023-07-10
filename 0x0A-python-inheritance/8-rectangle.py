#!/usr/bin/python3

""" A definition of Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Define Rectangle class"""
    def __init__(self, width, height):
        """ Initialize Rectangle class"""
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
