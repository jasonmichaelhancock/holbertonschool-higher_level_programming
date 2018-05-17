#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(text)
        a_file.seek(0, 2)
        return a_file.tell()
