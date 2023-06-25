#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for roman_char in roman_string:
        value = roman_values.get(roman_char, 0)

        if value == 0:
            return 0

        if value > prev_value:
            total -= 2 * prev_value

        total += value
        prev_value = value

    return total
