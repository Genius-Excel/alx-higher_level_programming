#!/usr/bin/python3

"""This module contains a fnction that writes to a file."""


def write_file(filename="", text=""):
    """This function writes to a file, creates it if it doesn't exist.
       or override an existing file with it's content.
       Args:
           filename (any): this represents the file to be written.
           test (any): this represents the contents to be written to the file.
       Returns:
           Number of characters written.
    """

    with open(filename, "w") as the_file:
        return the_file.write(text)
