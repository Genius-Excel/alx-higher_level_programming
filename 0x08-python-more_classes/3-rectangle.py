#!/usr/bin/python3

"""This module contains the definition of the class for a Rectangle"""


class Rectangle(object):
    """This class object respresnets the definition for the Rectangle class
        It has several methods the a defined the Area and other properties of
        the Rectangle class object.
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rec = '\n'.join('#' * self.__width for i in range(self.__height))

            return rec

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
