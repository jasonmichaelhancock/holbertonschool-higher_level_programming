#!/usr/bin/python3
def safe_print_division(a, b):
    c = 0
    try:
        c = a / b
        return(c)
    except:
        return(None)
    finally:
        if (b == 0):
            print("Inside Result: None")
        else:
            print("Inside Result: {:.1f}".format(c))
