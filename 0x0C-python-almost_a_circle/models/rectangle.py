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
        self.__width = value

    @property
    def height(self):
        """Return height of rectangle class"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle class"""
        self.__height = value

    @property
    def x(self):
        """Return x position of rectangle class"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x position of rectangle class"""
        self.__x = value

    @property
    def y(self):
        """Return y position of rectangle class"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y position of rectangle class"""
        self.__y = value
