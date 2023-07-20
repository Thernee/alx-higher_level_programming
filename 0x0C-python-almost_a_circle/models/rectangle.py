#!/usr/bin/python3

""" Module for class 'Triangle'
    - A subclass of the 'Base' class
"""
from models.base import Base


class Rectangle(Base):
    """ class 'Rectangle' that represents a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return width of rectangle class"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle class"""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return height of rectangle class"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle class"""
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return x position of rectangle class"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x position of rectangle class"""
        if not type(value) is int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return y position of rectangle class"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y position of rectangle class"""
        if not type(value) is int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
