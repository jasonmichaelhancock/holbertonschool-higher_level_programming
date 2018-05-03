#!/usr/bin/python3
class Square(object):
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return (self.__size) * (self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print(" " * self.__position[0])
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
