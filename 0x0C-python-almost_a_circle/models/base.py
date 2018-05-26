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

    def to_json_string(list_dictionaries):
        """Function returns JSON represeantion of dictionary. """
        if list_dictionaries is None:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)
