#!/usr/bin/python3


"""This module contains a function tha peforms addition.

   Args:
       a (int): this is the first operand of the operation.
       b (int): this is the second operand of the operation.

   Returns:
       the value of the sum of a and b in integer.
"""


def add_integer(a, b=98):
    """This function calculates the sum of two numbers.
       Returns: the sum of the numbers a and b in integer format.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
