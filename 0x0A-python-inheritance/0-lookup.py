#!/usr/bin/python3

"""This module contains a function that list ll the attributes
   and methdos of an object.
"""


def lookup(object):
    """this function returns all the available methods and
       and attributes of an object.

       Args:
           object (any): this is the object parameter of the function.
       Returns:
           a list of all methods and attributes.
    """


    return list(dir(object))
