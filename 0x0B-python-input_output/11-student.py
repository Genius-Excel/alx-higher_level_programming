#!/usr/bin/python3

"""This module contains a class that output the dictionary
   of its objects.
"""


class Student:
    """This class returns a dictionary info of the object
       Attributes:
           first_name (str): this represents the first name attribute.
           last_name (str): this represents the last name attribute.
           age (int): this represents the age attribute.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        # loop through the attrs and get the keys.
        new_json_dict = dict()
        for att_key in attrs:
            if hasattr(self, att_key):
                att_value = getattr(self, att_key)
                if isinstance(att_value, (int, str, list, dict)):
                    new_json_dict[att_key] = att_value
                elif isinstance(att_value, (tuple, set)):
                    new_json_dict[att_key] = list(att_value)
                elif hasattr(att_key, "__dict__"):
                    new_json_dict[att_key] = self.to_json(self)
                else:
                    new_json_dict[att_key] = None

        return new_json_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
