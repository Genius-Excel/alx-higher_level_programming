#!/usr/bin/python3


"""This module contains a class that raises an exception.
   and validates an integer
"""


class BaseGeometry:
    """This calss raises an exception and validated an integer"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        if not isinstance(name, str):
            raise TypeError("{} must be a string".format(name))


class Rectangle(BaseGeometry):
    """This class is a defintion of a rectangle class which inherits
       methods of the BaseGeometry class.
    """

    def __init__(self, width, height):
        # super().__init__()
        self.integer_validator("width", width)

        self.integer_validator("height", height)

        self.__height = height

        self.__width = width

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return (self.__width * self.__height)
