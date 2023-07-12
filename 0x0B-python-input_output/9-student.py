#!/usr/bin/python3

""" Defines class Student"""


class Student:
    """ Return dictionary representation of obj"""
    def __init__(self, first_name, last_name, age):
        """initialize Student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Return dictionary representation of Student class"""
        return self.__dict__
