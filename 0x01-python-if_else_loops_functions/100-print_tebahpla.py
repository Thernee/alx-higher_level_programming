#!/usr/bin/python3

num = 25
while num >= 0:
    if num % 2 != 0:
        print("{}".format(chr(97 + num)), end="")
    else:
        print("{}".format(chr(65 + num)), end="")
    num = num - 1
