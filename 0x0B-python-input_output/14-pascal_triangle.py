#!/usr/bin/python3
def pascal_triangle(n):
    outter = []
    if n <= 0:
        return outter
    for i in range(n):
        thelist = []
        for j in range(i + 1):
            if j == 0 or j == i:
                thelist.append(1)
            else:
                thelist.append(outter[i-1][j-1] + outter[i-1][j])
        outter.append(thelist)
    return outter
