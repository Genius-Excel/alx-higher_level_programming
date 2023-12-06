#!/usr/bin/python3

"""this module contains a function that returns a serilized
   dictionary of an object. 
"""


def class_to_json(obj):
    """This function serializes a class object to a JSON object
       Args:
           obj (any): this reprents the object of the class.
       Returns:
           a dictionary of a new JSON object.   
    """

    new_json_dict = dict()
    object_dic = obj.__dict__

    for key, value in object_dic.items():
        if isinstance(value, (int, list, dict, bool, str)):
            new_json_dict[key] = value
        elif isinstance(value, (tuple, set)):
            new_json_dict[key] = list(value)
        elif hasattr(value, "__dict__"):
            new_json_dict[key] = class_to_json(value)

    return new_json_dict