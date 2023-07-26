#!/usr/bin/python3

"""
   Doc for the base class 'Base' -
   A base class for all classes in the project
   Takes 1 argument (id)
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return JSON string representation of dicts"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of list of objects to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                my_list = [obj.to_dictionary() for obj in list_objs]
                json_file.write(Base.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """Return python representation of json string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create a new instance from dictionary"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(5, 5)
        elif cls.__name__ == "Square":
            new_instance = cls(5, 5)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """load from file"""
        filename = cls.__name__ + ".json"
        obj = []

        try:
            with open(filename, 'r') as f:
                str = f.read().strip()
                holder = cls.from_json_string(str)
                for elem in holder:
                    obj.append(cls.create(**elem))
        except Exception:
            return []

        return obj
