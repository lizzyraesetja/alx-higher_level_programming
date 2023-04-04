#!/usr/bin/python3

#This ia the Rectangle module.
#This module provides a simple Rectangle class with attribute width and hieight.
#Default values of both attributes are 0.

class Rectangle:
    """A Rectanagle class with attributes width and height"""
    def _int_(self,width=0,height=0):
        self.width = width
        self.height = height

        @property
        def width(self):
            return selft._width

        @width.setter
        def width(self,values):
            if type(value) is not int:
                raise TypeError('Width must be an ineger')
            if value < 0:
                raise ValueError('Width must >= 0')
            self._width = value

            @property
            def height(self):
                return self._height

            @height.setter
            def height(self,value):
                if type(value) is not int:
                    raise TypeError('height must be an integer')
                if value <0:
                    raise ValueError('height must be >=0)
                    self._height =value
