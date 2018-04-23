#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = dict(a_dictionary)
    for k in new_d.keys():
        new_d[k] *= 2
    return(new_d)
