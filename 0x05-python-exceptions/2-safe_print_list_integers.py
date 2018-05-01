#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    try:
        for i in range(x):
            if (type(my_list[i]) == int):
                print("{}".format(my_list[i]), end="")
                y += 1
        print("")
    except TypeError:
        print("")
        return(y)
    return(y)
