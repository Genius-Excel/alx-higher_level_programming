#!/usr/bin/python3

"""This module contains a class defintion of the Base models class"""


import json


class Base(object):
    """This is the class defition of the base model.

       Attributes:
           id (int): this represents the id of the class.
    """

    __nb_object = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        for obj in list_objs:
            cls.filename = "{}.json".format(obj.__class__.__name__)

        with open(cls.filename, "w") as file:
            file.write(cls.to_json_string(list_objs))