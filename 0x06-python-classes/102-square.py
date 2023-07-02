#!/usr/bin/python3

""" Defines a square class """


class Square:
    """ This is an empty square class """

    def __init__(self, size=0):
        """ Initializes the square
        Args:
            size (int): Given size of the square
        """
        self.size = size

    @property
    def size(self):
        """ Returns the current square size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter for the square size"""
        try:
            if not isinstance(value, int):
                raise TypeError
        except (TypeError, ValueError):
            raise TypeError("size must be an integer")
        else:
            self.__size = value
            if self.__size < 0:
                raise ValueError("size must be >= 0")

    def area(self):
        """ Returns the current square area """
        return self.__size * self.__size

    def __eq__(self, other):
        """ Implements the == operator """
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """ Implements the != operator """
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __lt__(self, other):
        """ Implements the < operator """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """ Implements the <= operator """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """ Implements the > operator """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """ Implements the >= operator """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
