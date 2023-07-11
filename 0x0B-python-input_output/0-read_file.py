#!/usr/bin/python3

""" A functions that reads from a text file"""


def read_file(filename=""):
    """ Define read_file function"""
    with open(filename, 'r', encoding="utf-8") as r_file:
        content = r_file.read()
        print(content, end="")
