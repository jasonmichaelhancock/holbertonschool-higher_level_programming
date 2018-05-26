#!/usr/bin/python3
"""
Module defines base class.
"""
import json


class Base:
    """
    This is the Base class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize the Base Class."""
        self.id = id
        if self.id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Function returns JSON represeantion of dictionary. """
        if list_dictionaries is None:
            return ("[]")
        if len(list_dictionaries) == 0:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a JSON string rep of list_objs to file."""
        filename = "{:s}.json".format(cls.__name__)
        content = []
        for i in range(len(list_objs)):
            content.append(cls.to_dictionary(list_objs[i]))
        with open(filename, mode = 'w', encoding = 'utf-8') as a_file:
            a_file.write(cls.to_json_string(content))

    @staticmethod
    def from_json_string(json_string):
        """Function returns a list of a JSON string rep."""
        if json_string is None:
            return ("[]")
        if (json_string) == []:
            return ("[]")
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
