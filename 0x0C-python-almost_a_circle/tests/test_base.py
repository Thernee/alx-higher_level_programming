#!/usr/bin/python3

""" Module for a unittest subclass for testing 'Base' class
    - a class which will be the base of all classes in this project
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ A class to test 'Base' class"""

    def test_empty_base(self):
        """Test empty 'Base' class multiple times"""
        test1 = Base()
        self.assertEqual(test1.id, 1)

        test2 = Base()
        self.assertEqual(test2.id, 2)

        test3 = Base()
        self.assertEqual(test3.id, 3)

    def test_incorrect_input(self):
        """ Test 'Base' with incorrect input"""
        self.assertRaises(TypeError, Base("string"))

        self.assertRaises(TypeError, Base(None))

    def test_correct_input(self):
        """ Test 'Base' with correct values"""
        test1 = Base(100)
        self.assertEqual(test1.id, 100)

        test2 = Base(13)
        self.assertEqual(test2.id, 13)


if __name__ == "__main__":
    unittest.main()
