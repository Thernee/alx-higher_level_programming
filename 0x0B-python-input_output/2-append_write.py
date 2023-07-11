#!/usr/bin/python3

""" A function that appends string to a text file"""


def append_write(filename="", text=""):
    """ Define appnd_write function"""
    with open(filename, 'a', encoding="utf-8") as a_file:
        initial = a_file.tell()
        a_file.write(text)
        if initial == a_file.tell():
            return initial
        return a_file.tell() - initial
