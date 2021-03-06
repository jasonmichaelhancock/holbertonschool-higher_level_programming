#!/usr/bin/python3
"""
Module documentation.
"""


from models.base import Base


class Rectangle(Base):
    """
    This clas inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x value."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x value."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y value."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y value of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Function sets the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Function prints the rectangle."""
        if self.width == 0:
            return
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Function returns string rep of the display function."""
        return "[Rectangle] (" + str(self.id) + ") " \
            + str(self.x) + "/" + str(self.y) + " - " \
            + str(self.width) + "/" + str(self.height)

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        if args is not None and len(args) > 0:
            cnt = 0
            attrs = ["id", "width", "height", "x", "y"]
            for arg in args:
                setattr(self, attrs[cnt], args[cnt])
                cnt += 1
        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Adds items to a_dict."""
        a_dict = {}
        key = ["id", "width", "height", "x", "y"]
        for i in range(len(key)):
            if key[i] == "id":
                a_dict[key[i]] = self.id
            if key[i] == "width":
                a_dict[key[i]] = self.width
            if key[i] == "height":
                a_dict[key[i]] = self.height
            if key[i] == "x":
                a_dict[key[i]] = self.x
            if key[i] == "y":
                a_dict[key[i]] = self.y
        return a_dict
