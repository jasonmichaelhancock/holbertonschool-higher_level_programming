#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_input(self):
        with self.assertRaises(TypeError):
            max_integer(["Jason", 4, 9])

    def test_input2(self):
        with self.assertRaises(TypeError):
            max_integer([[1, 2, 3], 4, 9])

    def test_input3(self):
        with self.assertRaises(TypeError):
            max_integer([(1, 2, 3), 4, 9])

    def test_input4(self):
        with self.assertRaises(TypeError):
            max_integer([{1:"a", 2:"b", 3:"c"}, 4, 9])

    def test_output(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4], 4.4)
        self.assertEqual(max_integer([1.1, 2.2, 3.3, -4.4] 3.3)
