#!/usr/bin/python3
"""
Contains tests for Rectangle class - Task 2
Focus is on:
- setting private instance attributes in the constructor using
  getters and setters
- calling super()__init__() to set public instance id attribute
"""

import unittest
import inspect

from models.base import Base
from models import square
Square = square.Square

class TestSquaredocs(unittest.TestCase):
    """Tests for documentation of class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.square_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_module_docstr(self):
        """Tests for docstring"""
        self.assertTrue(len(square.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)

def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.square_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

class TestRectangle(unittest.TestCase):
    """ Tests functionality of class"""

    def test_properties(self):
        """Tests all setters and getters"""
        Base._Base__nb_objects = 0
        s_1 = Square(1)
        self.assertEqual(s_1.size, 1)
        self.assertEqual(s_1.x, 0)
        self.assertEqual(s_1.y, 0)

        s_1.x = 10
        s_1.y = 10
        self.assertEqual(s_1.x, 10)
        self.assertEqual(s_1.y, 10)

        """ Tests functionality of super()_int_() call"""

    def test_id_none(self):
        """Tests id not passed in"""
        s_2 = Square(1)
        s_2 = Square(1)
        self.assertEqual(s_2.id, 2)

    def test_id_assigned(self):
        """Tests id passed in"""
        s_3 = Square(1, 1, 1, 88)
        self.assertEqual(s_3.id, 88)

    def test_nb_object_increment(self):
        """Tests private class attribute incrementation"""
        s_4 = Square(1)
        self.assertEqual(s_4.id, 3)

    """Tests number of arguments passed in"""
    def test_too_many_args(self):
        """Tests entering too many args to instantiate object"""
        with self.assertRaises(TypeError):
            s = Square(1, 2, 3, 4, 5, 6)

    def test_too_few_args(self):
        """Tests entering too few args to instantiate object"""
        with self.assertRaises(TypeError):
            s = Square()

    def test_update_no_args(self):
        """ Tests for no args passed in update method"""
        s = Square(1, 2, 3, 4)
        s.update()
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")

    def test_update_too_many_args(self):
        """ Tests for too many args passed in update method"""
        s = Square(1, 2, 3, 4)
        s.update(1, 1, 1, 1, 5)
        self.assertEqual(str(s), "[Square] (1) 1/1 - 1")

    def test_update_args_with_string(self):
        """ Test passing a string (wrong type) for update method """
        s = Square(1)
        with self.assertRaises(TypeError):
            s.update(2, "test")
        with self.assertRaises(TypeError):
            s.update(2, 3, "test")
        with self.assertRaises(TypeError):
            s.update(2, 3, 4, "test")
        with self.assertRaises(TypeError):
            s.update(2, 3, "test", "doubletest")

    def test_update_args(self):
        """ Test update method with args for each attr - regular use"""
        s = Square(1, 1, 1, 1)
        self.assertEqual(str(s), "[Square] (1) 1/1 - 1")
        s.update(2)
        self.assertEqual(str(s), "[Square] (2) 1/1 - 1")
        s.update(2, 3)
        self.assertEqual(str(s), "[Square] (2) 1/1 - 3")
        s.update(2, 3, 4)
        self.assertEqual(str(s), "[Square] (2) 4/1 - 3")
        s.update(2, 3, 4, 5)
        self.assertEqual(str(s), "[Square] (2) 4/5 - -3")


