#!/usr/bin/python3

""" A functions that writes to a text file"""


def write_file(filename="", text=""):
    """ Define write_file function"""
    with open(filename, 'w', encoding="utf-8") as w_file:
        initial = w_file.tell()
        w_file.write(text)
        if initial == w_file.tell():
            return initial
        return w_file.tell()
