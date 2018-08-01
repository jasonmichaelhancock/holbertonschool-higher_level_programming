#!/usr/bin/python3
"""Find peak integer in list."""


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    compnum = list_of_integers[0]
    for x in list_of_integers:
        if x >= compnum:
            compnum = x
    return compnum
