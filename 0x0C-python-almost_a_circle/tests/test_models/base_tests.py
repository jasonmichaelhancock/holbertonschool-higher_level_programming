#!/usr/bin/python3
"""testing Base class code"""
import pep8
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseMethods(unittest.TestCase):
    """class with tests"""


    def test_check_id(self):
        """checking id"""
        r1 = Base()
        self.assertEqual(r1.id, 1)
        r2 = Base(12)
        self.assertEqual(r2.id, 12)
        r3 = Base()
        self.assertEqual(r3.id, 2)
        r4 = Base(-1)
        self.assertEqual(r4.id, -1)

    def test_to_js_str(self):
        """checking the dumps method"""

        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_doc(self):
        """testing docstring"""

        self.assertIsNotNone(Base.__doc__)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py', 'models/rectangle.py', 'models/square.py'])
        self.assertEqual(result.total_errors, 0)




    if __name__ == '__main__':
        unittest.main()
