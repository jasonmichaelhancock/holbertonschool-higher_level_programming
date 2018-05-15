#!/usr/bin/python3
def text_indentation(text):
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("{}\n".format(text[i]))
            i += 1
            while text[i] == " ":
                i += 1

        elif text[i] == " " and (text[i - 1] == "." or text[i - 1] == "?" or text[i - 1] == ":"):
            while text[i] == " ":
                i = i + 1
        else:
            print("{}".format(text[i]), end = "")
            i += 1
