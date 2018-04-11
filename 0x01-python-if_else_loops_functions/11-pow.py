#!/usr/bin/python3
def pow(a, b):
    a = int(a)
    b = int(b)
    result = 1
    for _ in range(b):
        result *= a
    return result
