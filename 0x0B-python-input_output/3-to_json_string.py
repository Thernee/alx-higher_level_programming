#!/usr/bin/python3

""" A function that returns JSON repr. of an object"""
import json


def to_json_string(my_obj):
    """ Define to_json_string function"""
    return json.dumps(my_obj)
