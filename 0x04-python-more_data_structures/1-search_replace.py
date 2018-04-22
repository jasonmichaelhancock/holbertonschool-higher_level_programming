#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in range(len(my_list)):
        if my_list[i] == search:
            del my_list[i]
            my_list.insert(i, replace)
    return(my_list)
