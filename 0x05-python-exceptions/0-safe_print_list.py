#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            y += 1
        print("")
    except IndexError:
        print("")
        return(y)
    return(y)
