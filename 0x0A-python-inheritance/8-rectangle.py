#!/usr/bin/python3
"""
Module documentation.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class for strange squares"""

    def __init__(self, width, height):
        """Creates a new square"""
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
