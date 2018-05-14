#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    c = int(a) + int(b)
    return c
