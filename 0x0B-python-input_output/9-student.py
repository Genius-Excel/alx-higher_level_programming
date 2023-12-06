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

    def to_json(self):
        new_json_dict = dict()
        class_obj_dict = self.__dict__

        for key, value in class_obj_dict.items():
            if isinstance(value, (int, str, dict, list)):
                new_json_dict[key] = value
            elif isinstance(value, (set, tuple)):
                new_json_dict[key] = list(value)
            elif hasattr(value, "__dict__"):
                new_json_dict[key] = self.to_json(self)

        return new_json_dict
