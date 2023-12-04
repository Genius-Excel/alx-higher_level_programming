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
