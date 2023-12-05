#!/usr/bin/python3


"""This module contains a function that adds a new attribute"""


def add_attribute(obj, att_name, att_value):
    """This function adds a new attribute to an object.

       Args:
           obj (any): this is an object of the class for the new attribute.
           att_name (any): this represents the attribute name
           att_value (any0: this is the value to be assigned to attr_name

       Returns:
           None
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add a new attribute")

    if not att_name or not att_value:
        raise TyoeError("can't add a new attribute")

    setattr(obj, att_name, att_value)
