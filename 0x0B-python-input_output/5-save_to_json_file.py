#!/usr/bin/python3

"""this module contains a function that writes a serialized
   JSON object to a file.
"""

import json


def save_to_json_file(my_obj, filename):
    """This function writes and saves a JSON object to a file.
       Args:
           my_obj (any): JSON object to be serialized.
           filename (any): This represents the file to be written to.
    """
    with open(filename, "w") as the_file:
        return the_file.write(json.dumps(my_obj))
