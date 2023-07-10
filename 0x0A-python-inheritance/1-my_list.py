#!/usr/bin/python3

""" An implememtation of MyList subclass"""


class MyList(list):
    """ An implememtation of MyList subclass"""
    def __init__(self):
        """ Initialize the MyList subclass"""
        self.list = []

    def print_sorted(self):
        """ Print a sorted list"""
        print(sorted(self))
