#!/usr/bin/python3
"""This is the "Rectangle" module.

This module provides a simple Rectangle class."""

class Rectangle:
    """A Rectangle class with attributes width and height, and methods area and perimiter."""

    def _int_(self, width=0, height=0):
        self.width = width
        self.height = height

        @property
        def width(self):
            return self._width

        @width.setter
        def.width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <0:
                raise ValueError("width must be >= 0")
            self._width = value

        @property
        def height(self):
            return self._height

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value < 0
            raise ValueError("Height must be >0")
        self._height = value

        def area(self):
            return self._width * self._height

        def perimiter(self):
            if self._width is not 0 or self._height is 0:
                return 0
            return (2* self.width) + (2 * selft.height)
