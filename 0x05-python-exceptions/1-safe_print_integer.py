#!/usr/bin/python3

def safe_print_integer(value):

    status = 0
    try:
        print("{:d}".format(int(value)))
    except ValueError:
        status = 0
    else:
        status = 1

    if status == 1:
        return True
    elif status == 0:
        return False
