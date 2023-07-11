#!/usr/bin/python3

""" A definition of Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Define Square class"""
    def __init__(self, size):
        """ Initialize Square class"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return area of the rectangle."""
        return self.__size * self.__size

    def __str__(self):
        """string reprsentation of rectangle."""
        s1 = self.__size
        s2 = self.__size
        return (f"[Square] {s2}/{s1}")
