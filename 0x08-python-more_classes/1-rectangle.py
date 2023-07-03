#!/usr/bin/python3

""" Defines a rectangle class."""


class Rectangle:
    """ The rectangle class."""
    def __init__(self, width=0, height=0):
        """ Initializes the rectangle

        Args:
            width (int): Given size of the rectangle
            height (int): Given size of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """ Returns the current Rectangle height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for the rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    @property
    def width(self):
        """ Returns the current Rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for the rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
