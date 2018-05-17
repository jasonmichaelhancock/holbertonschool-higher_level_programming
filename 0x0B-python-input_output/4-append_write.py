#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as a_file:
        a_file.seek(0, 2)
        y = a_file.tell()
        a_file.write(text)
        a_file.seek(0, 2)
        x = a_file.tell()
        return x - y
