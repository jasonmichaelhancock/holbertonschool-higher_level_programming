#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    c = len(sys.argv) - 1
    if c == 0:
        print("{:d}".format(c))
    elif c == 1:
        print("{:d}".format(str(sys.argv[1])))
    else:
        x = 0
        for i in range(1, c + 1):
            x += int(sys.argv[i])
        print("{:d}".format(x))
