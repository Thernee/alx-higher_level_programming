#!/usr/bin/python3

def islower(c):

    temp = ord(c)

    for number in range(97, 123):
        if temp == number:
            return True

    return False
