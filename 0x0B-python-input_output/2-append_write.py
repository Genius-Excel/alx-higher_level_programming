#!/usr/bin/python3

"""This module conains a fnction that appends to an existing file."""


def append_write(filename="", text=""):
    """This function appends a text to an existing file.
       Args:
           filename (any): this represents the file name.
           text (any): this is represents the text to be added to the file.
       Returns:
           Number of characters appended to the file.
    """

    with open(filename, "a") as the_file:
        return the_file.write(text)
