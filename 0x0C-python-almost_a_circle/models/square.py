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
