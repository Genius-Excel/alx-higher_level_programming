#!/usr/bin/python3


"""This module cntans a funcion that checks the nstnce of an object."""


def is_same_class(obj, a_class):
    """This function checks if an object is  memeber of a class

       Args:
           obj (any): object param to be checked for membership of a class.
           a_class (any):class parameter of the class.

       Returns:
           True if obj is member of a_class else False.
    """

    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
