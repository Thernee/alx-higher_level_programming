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

    def area(self):
        """Return area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """string reprsentation of rectangle."""
        height = self.__height
        width = self.__width
        return (f"[Rectangle] {width}/{height}")
