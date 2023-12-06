#!/usr/bin/python3

"""This module contains a function that serializes an object with JSON"""

import json


def to_json_string(object):
    """This function serializes an object to a JSON string
       Args:
           object (any): Object to be serialized.
       Returns:
           JSON object that has been serialized.
    """

    return (json.dumps(object))
