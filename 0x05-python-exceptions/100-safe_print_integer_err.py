#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        if not isinstance(value, int):
            raise Exception
        return True
    except Exception:
        sys.stderr.write("Exception: Unknown format code 'd' for object of type 'str'\n")
        return False
