#!/usr/bin/python3
""" module 100-my_int contains class MyInt, a subclass of int """


class MyInt(int):
    """ defines class MyInt """

    def __eq__(self, other):
        """ == now acts like != """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ != now acts like == """
        return int.__eq__(self, other)
