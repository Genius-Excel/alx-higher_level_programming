#!/usr/bin/python3


"""This module contains a function that checks the memebrship of an object."""


def inherits_from(obj, a_class):
    """This function checks if n objects is an instance of a class.

       Args:
           obj (any): this is the object whose memebrship is to be checked.
           a_class (any): this represents the class for which obj is checked
                          as a memeber of it's class.
       Returns:
        True if obj is an instance or object of the a_class.
    """

    if issubclass(a_class, a_class.__bases__):
        return True

    return False
