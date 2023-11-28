#!/usr/bin/python3


"""This module contains a function tha prints the name of user.
   Args:
       first_name (str): this reperesents the first name of the user
       last_name (str): this represents the last name of the user.
"""


def say_my_name(first_name, last_name=""):
    """This function prints the first and last names of a user.
       Returns: None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
