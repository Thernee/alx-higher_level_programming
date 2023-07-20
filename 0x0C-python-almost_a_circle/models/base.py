#!/usr/bin/python3

"""
   Doc for the base class 'Base' -
   A base class for all classes in the project
   Takes 1 argument (id)
"""


class Base():
    """ A base class for all classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Define 'Base' class"""
        if id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id
