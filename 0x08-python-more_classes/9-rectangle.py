#!/usr/bin/python3

""" Defines a rectangle class."""


class Rectangle:
    """ The rectangle class."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes the rectangle

        Args:
            width (int): Given size of the rectangle
            height (int): Given size of the rectangle
        """
        type(self).number_of_instances += 1
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

    def area(self):
        """ Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (int(self.__width) + int(self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the biggest area
        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        """
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.
        Args:
            size (int): size of the new Rectangle.
        """
        return cls(size, size)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        holder = ""
        holder2 = []
        if self.__width == 0 or self.__height == 0:
            return holder
        else:
            for _ in range(self.__height):
                temp = self.__width
                while temp > 0:
                    holder2.append(self.print_symbol)
                    temp -= 1
                holder2.append("\n")
        holder2.pop()
        return ("".join(str(elem) for elem in holder2))

    def __repr__(self):
        """Returns a string representation of the rectangle for recreation."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ prints message for rectangle deletion"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
