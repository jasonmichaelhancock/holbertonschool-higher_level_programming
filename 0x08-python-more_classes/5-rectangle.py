#!/usr/bin/python3
class Rectangle():
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def __del__(self):
        print("Bye rectangle...")

    def area(self):
        return (self.__width) * (self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return(0)
        else:
            return ((self.__width) + (self.__height)) * 2

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return("")
        else:
            return ((("#" * self.__width) + ('\n')) * (self.__height - 1)) \
                + ("#" * self.__width)

    def __repr__(self):
        return("Rectangle({}, {})".format(self.width, self.height))
