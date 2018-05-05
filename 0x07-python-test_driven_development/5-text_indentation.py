#!/usr/bin/python3
def text_indentation(text):
    i = 0
    for i in range(len(text)):
        if (text[i - 1] == "." or text[i - 1] == "?" or text[i - 1] == ":") and text[i] == " ":
            continue
        elif text[i] == "." or text[i] == "?" or text[i] == ":":
            print("{}".format(text[i]))
        else:
            print("{}".format(text[i]), end = "")
        i += 1
