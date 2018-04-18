#!/usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)
    result = list()
    for letter in my_string:
        if letter.lower() not in 'cC':
            result.append(letter)
    return ''.join(result)
