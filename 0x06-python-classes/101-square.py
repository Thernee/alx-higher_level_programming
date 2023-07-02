#!/usr/bin/python3

"""This class represents a square"""


class Square:
    """This class represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square.

        Args:
            size (int): Size of the square (default is 0).
            position (tuple): Position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of the square.

        Args:
            value (int): Size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position of the square.

        Args:
            value (tuple): Position of the square.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints a representation of the square."""
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """Returns a string representation of the square."""
        square_str = ""
        if self.size == 0:
            square_str += "\n"
        else:
            for _ in range(self.position[1]):
                square_str += "\n"
            for _ in range(self.size):
                square_str += " " * self.position[0] + "#" * self.size + "\n"
        return square_str.rstrip()
