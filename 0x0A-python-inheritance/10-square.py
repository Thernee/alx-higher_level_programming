#!/usr/bin/python3

""" A definition of Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Define Square class"""
    def __init__(self, size):
        """ Initialize Square class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return area of the rectangle."""
        return self.__size * self.__size
