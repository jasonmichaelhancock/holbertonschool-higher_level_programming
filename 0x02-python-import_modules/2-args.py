#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    c = len(sys.argv) - 1
    if c == 0:
        print("{:d} arguments.".format(c))
    elif c == 1:
        print("{:d} argument:".format(c))
        print("1: {}".format(str(sys.argv[1])))
    else:
        print("{:d} arguments:".format(c))
        for i in range(1, c + 1):
            print("{}: {}".format(i, str(sys.argv[i])))
