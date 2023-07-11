#!/usr/bin/python3

""" A function that writes a JSON obj to a text file"""
import json


def load_from_json_file(filename):
    """ Define save_to_json_file function"""
    with open(filename, 'r', encoding='utf-8') as s_file:
        obj = json.load(my_obj, s_file)
    return obj
