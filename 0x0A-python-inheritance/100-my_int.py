#!/usr/bin/python3

"""MyInt class"""


class MyInt(int):
    """MyInt rebel class. has == and != operators inverted """

    def __init__(self, value):
        """ Initialize MyInt"""
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, value):
        """chnages == to !="""
        return self.real != value

    def __ne__(self, value):
        """changes != to =="""
        return self.real == value
