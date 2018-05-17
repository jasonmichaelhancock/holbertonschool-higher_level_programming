#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    line_count = 0
    with open(filename, encoding='utf-8') as a_file:
        for a_line in a_file:
            if nb_lines <= 0:
                print("{}".format(a_line), end="")
            elif (line_count < nb_lines):
                print("{}".format(a_line), end="")
            line_count += 1
    return line_count
