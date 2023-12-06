#!/usr/bin/python3

"""This module contians a function that locates a specific string
   and appends to the file.
"""


def append_after(filename="", search_string="", new_string=""):
    """This function searches for a specific string and appends
       a new string to file.
       Args:
           filename (any): this represents the filename.
           search_string (any): this represents the string to be located.
           new_string (any): this represents the new string to be appended.
       Returns:
           None
    """
    # open the file for read mode if it exists.
    with open(filename, "r") as my_file:
        read_lines = my_file.readlines()

    with open(filename, "w") as the_file:
        for line in read_lines:
            the_file.write(line)
            if search_string in line:
                the_file.write(new_string)
