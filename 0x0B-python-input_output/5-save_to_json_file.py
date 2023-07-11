#!/usr/bin/python3

""" A function that writes a JSON obj to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """ Define save_to_json_file function"""
    with open(filename, 'w', encoding='utf-8') as w_file:
        holder = json.dump(my_obj, w_file)
    return holder
