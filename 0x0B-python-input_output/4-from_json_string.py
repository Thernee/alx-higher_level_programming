#!/usr/bin/python3

""" A function that covert str to JSON obj of an object"""
import json


def from_json_string(my_str):
    """ Define from_json_string function"""
    return json.loads(my_str)
