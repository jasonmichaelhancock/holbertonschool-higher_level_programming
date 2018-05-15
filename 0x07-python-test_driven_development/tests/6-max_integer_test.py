#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        result = max_integer([1, 4, 3, 2])
        self.assertEqual(result, 4)
        result = max_integer([12, 9, 7, 2])
        self.assertEqual(result, 12)
