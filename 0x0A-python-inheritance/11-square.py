#!/usr/bin/python3
""" module Rectangle inherits Basegeometry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defines class Square """

    def __init__(self, size):
        """ initializes empty Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ returns unofficial string representation of Square """
        return "[Square] {}/{}".format(self.__size, self.__size)
