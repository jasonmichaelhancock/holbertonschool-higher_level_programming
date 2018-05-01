#!/usr/bin/python3
i = 0
j = 1
l = 1
while i < 8:
    j = l
    while j < 10:
        print('{:d}{:d}, '.format(i, j), end="")
        j += 1
    l += 1
    i += 1
print("89")
