#!/usr/bin/python3

""" Defines class Student"""


class Student:
    """ Return dictionary representation of obj"""
    def __init__(self, first_name, last_name, age):
        """initialize Student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return dictionary representation of Student class"""
        if attrs is None:
            return self.__dict__
        class_dict = self.__dict__
        attrs_dict = dict()

        for num in range(len(attrs)):
            if type(attrs[num]) is str and attrs[num] in class_dict:
                attrs_dict[attrs[num]] = class_dict[attrs[num]]

        return attrs_dict
