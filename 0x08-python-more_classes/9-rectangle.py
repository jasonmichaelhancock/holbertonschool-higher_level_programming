#!/usr/bin/python3
class Rectangle():
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1
        type(self).print_symbol

    def __del__(self):
        print("Bye rectangle…")
        type(self).number_of_instances -= 1

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
            print("")
        return (((str(self.print_symbol) * self.__width) + ('\n')) * (self.__height - 1)) + (str(self.print_symbol) * self.__width)

    def __repr__(self):
        return("Rectangle({}, {})".format(self.width, self.height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        x = rect_1.area()
        y = rect_2.area()
        if x >= y:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
