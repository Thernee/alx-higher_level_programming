#!/usr/bin/python3

""" Module for class 'Square'
     - A subclass of the 'Rectangle' class
 """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class 'Square' that represents a square."""
    def __init__(self, size, x=0, y=0, id=None) -> None:
        """Initialize the Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of Square instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """returns size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setr size of Square"""
        self.width = value
        self.height = value
