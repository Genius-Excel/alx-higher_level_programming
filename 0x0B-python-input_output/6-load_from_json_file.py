#!/usr/bin/python3

"""This module contains a function that reads a JSON file
   and desrializes the JSON object.
"""

import json


def load_from_json_file(filename):
    """This creates an object from a JSON file and returns the object
       Args:
           filename (any): this represents the JSON file to be read
       Returns:
           The JSON object read from the file.
    """

    with open(filename, "r") as the_file:
        json_object = json.load(the_file)

        return json_object
