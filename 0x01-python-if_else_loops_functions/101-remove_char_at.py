#!/usr/bin/python3

def remove_char_at(str, n):
    if str:
        if n >= len(str) or n < 0:
            return str
        new_str = ""
        for char in str:
            if char != str[n]:
                new_str += char
        return new_str
