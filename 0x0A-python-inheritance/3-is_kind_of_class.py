#!/usr/bin/python3


"""This module contains function that checks the kind of object."""


def is_kind_of_class(obj, a_class):
    """This function checks if an object is a kind of a class.

       Args:
           obj (any): this is the objects to be checked for mebership.
           a_class (any): this is the class to be checked for instance of obj
       Returns:
           True if the obj is a kind of the a_class else False.
    """

    if isinstance(obj, a_class) or isinstance(obj, a_class.__bases__)\
       and type(obj) is a_class.__bases__:
        return True

    return False
