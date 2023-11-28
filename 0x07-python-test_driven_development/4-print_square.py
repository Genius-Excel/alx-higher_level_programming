#!/usr/bin/python3


"""This module contains a function that prints a square

   Args:
       size (int): this represents the dimension of the squre.
"""


def print_square(size):
    """this function prints a squre wit the '#' symbol.
       Returns: None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
