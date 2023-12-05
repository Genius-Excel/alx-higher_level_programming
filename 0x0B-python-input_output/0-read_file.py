#!/usr/bin/python3

"""This module contians a function that read the content of a file."""


def read_file(filename=""):
    """This function reads a file and prints to standard output.
       Args:
           filename (any): this represents the file to be read.
        Returns:
            None
    """

    with open(filename, "r") as the_file:
        for line in the_file:
            print(line)
