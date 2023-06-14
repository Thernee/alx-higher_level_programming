#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    if set_1:
        if set_2:
            holder = set_1 | set_2
            return sorted(holder)
        return sorted(set_1)

    return sorted(set_2)
