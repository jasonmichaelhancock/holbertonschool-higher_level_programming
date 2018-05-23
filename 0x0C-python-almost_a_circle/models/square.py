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
            raise ValueError("width must be >= 0")
        self.width = value
        self.height = value
