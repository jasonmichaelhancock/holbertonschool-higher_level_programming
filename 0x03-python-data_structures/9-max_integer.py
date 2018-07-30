#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    if len(my_list) == 1:
        return my_list[0]
    compnum = my_list[0]
    for x in my_list:
        if x >= compnum:
            compnum = x
    return compnum
