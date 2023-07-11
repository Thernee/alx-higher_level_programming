#!/usr/bin/python3

""" A function that writes a JSON obj to a text file"""
from sys import argv


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    my_list = []
    try:
        my_list = load_from_json_file("add_item.json")
    except Exception:
        pass

    if len(argv) > 1:
        for num in range(1, len(argv)):
            my_list.append(argv[num])

    save_to_json_file(my_list, "add_item.json")


