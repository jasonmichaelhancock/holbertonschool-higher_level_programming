#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set(my_list)
    new_list = list(new_set)
    result = 0
    for i in range(0, len(new_list)):
        result = result + new_list[i]
    return(result)
