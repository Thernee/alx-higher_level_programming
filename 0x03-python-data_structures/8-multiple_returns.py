#!/usr/bin/python3

def multiple_returns(sentence):

    length = len(sentence)
    if sentence:
        my_tuple = (length, sentence[0])
        return my_tuple

    else:
        sentence = None
        my_tuple = (length, sentence)
        return my_tuple
