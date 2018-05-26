#!/usr/bin/python3
"""
Module documentation
"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Function returns string rep of the display function."""
        return "[Square] (" + str(self.id) + ") " \
            + str(self.x) + "/" + str(self.y) + " - " \
            + str(self.width)

    @property
    def size(self):
        """Gets the size."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        if args is not None and len(args) > 0:
            c = 0
            attrs = ["id", "size", "size", "x", "y"]
            for arg in args:
                setattr(self, attrs[c], args[c])
            c += 1
        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Adds items to a_dict."""
        a_dict = {}
        key = ["id", "size", "size", "x", "y"]
        for i in range(len(key)):
            if key[i] == "id":
                a_dict[key[i]] = self.id
            if key[i] == "width":
                a_dict[key[i]] = self.size
            if key[i] == "x":
                a_dict[key[i]] = self.x
            if key[i] == "y":
                a_dict[key[i]] = self.y
        return a_dict
