#!/usr/bin/python3

"""This module contians a function that locates a specific string
   and appends to the file. 
"""


def append_after(filename="", search_string="", new_string=""):
    # open the file for read mode if it exists.
    with open(filename, "r") as my_file:
        read_lines = my_file.readlines()

    with open(filename, "w") as the_file:
        for line in read_lines:
            the_file.write(line)
            if search_string in line:
                the_file.write(new_string)