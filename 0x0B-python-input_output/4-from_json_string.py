#!/usr/bin/python3

"""This module contains  function that deserializes a JSON string"""


import json


def from_json_string(my_str):
    """This function deserializes a JSON string
       Args:
           my_string (any): This represents the JSON string.
       Returns:
           A deserialised JSON object string.    
    """

    return (json.loads(my_str))