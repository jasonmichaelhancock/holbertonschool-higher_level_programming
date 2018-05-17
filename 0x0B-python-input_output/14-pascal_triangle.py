#!/usr/bin/python3
def pascal_triangle(n):
    l = [1]
    for i in range(n):
        newlist = []
        newlist.append(l[0])
        for i in range(len(l) - 1):
            newlist.append(l[i] + l[i+1])
        newlist.append(l[-1])
        l.append(newlist)
    return l
