#!/usr/bin/python3
def multiple_returns(sentence):
    a = ()
    if sentence is None or sentence is "":
        a = (0, None)
    else:
        b = len(sentence)
        c = sentence[0]
        a = (b, c)
    return a
