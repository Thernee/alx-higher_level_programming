#!/usr/bin/python3

""" Defines class_to_json function"""


def class_to_json(obj):
    """ Return dictionary representation of obj"""
    return obj.__dict__
