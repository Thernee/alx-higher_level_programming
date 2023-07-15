#!/usr/bin/python3

import unittest
"""
    Unittests for max_integer() using TestMaxInteger class
    TestMaxInteger is a subclass of unittest.TestCase

"""


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer()"""

    def test_empty_list(self):
        """test an empty list."""
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_sorted_list(self):
        """test sorted list of integers."""
        sorted = [2, 3, 4, 5]
        self.assertEqual(max_integer(sorted), 5)

    def test_unsorted_list(self):
        """test an unsorted list of integers."""
        unsorted = [5, 2, 4, 3]
        self.assertEqual(max_integer(unsorted), 5)

    def test_single_element_list(self):
        """test a list with single element."""
        single_elem = [3]
        self.assertEqual(max_integer(single_elem), 3)

    def test_float(self):
        """test a list of all float values."""
        float_list = [2.85, 3.40, -8.103, 21.24, 9.0]
        self.assertEqual(max_integer(float_list), 21.24)

    def test_combination(self):
        """test a list with combination of ints and floats."""
        comb_list = [2.53, 18.5, -9, 15, 5]
        self.assertEqual(max_integer(comb_list), 18.5)

    def test_single_string(self):
        """test a string."""
        string = "A sample string"
        self.assertEqual(max_integer(string), 't')

    def test_list_of_strings(self):
        """test a list of strings."""
        strings = ["Here", "to", "test", "this"]
        self.assertEqual(max_integer(strings), "to")

    def test_empty_string(self):
        """test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
