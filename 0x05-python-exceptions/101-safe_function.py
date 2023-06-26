#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        holder = fct(*args)
    except BaseException:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
    else:
        return holder
