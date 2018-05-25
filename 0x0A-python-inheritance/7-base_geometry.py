#!/usr/bin/python3
"""module documentation
"""


class BaseGeometry:
    
    def area(self):
        """function finds the area"""
        raise Exception("area() is not implemented")
        
    def integer_validator(self, name, value):
        """function validates value and name"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than zero".format(name))
