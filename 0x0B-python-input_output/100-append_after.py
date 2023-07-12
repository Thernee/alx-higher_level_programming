#!/usr/bin/python3

""" A function that inserts line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """ Define appnd_after function"""
    with open(filename, 'r', encoding="utf-8") as r_file:
        holder = r_file.readlines()
        text_holder = ""

        for line in holder:
            text_holder += line
            if search_string in line:
                text_holder += new_string

    with open(filename, 'w', encoding="utf-8") as w_file:
        w_file.write(text_holder)
