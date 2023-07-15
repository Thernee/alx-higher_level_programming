#!/usr/bin/python3


"""Defines a text_indentation function
    Takes one argument (text)
"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    new_text = ""
    skip_space = True
    for char in text:
        if char == " " and skip_space:
            continue
        elif char in ".?:":
            new_text += char + "\n\n"
            skip_space = True
        elif char == "\n":
            new_text += char
            skip_space = True
        else:
            new_text += char
            skip_space = False

    print(new_text, end="")
