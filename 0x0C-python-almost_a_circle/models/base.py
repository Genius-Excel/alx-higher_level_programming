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

    def change_to_dictionary(self, data_obj):
        pass

    @classmethod
    def save_to_file(cls, list_objs):
        cls.json_obj_list = []
        cls.filename = "{}.json".format(cls.__name__)

        for cls_obj in list_objs:
            cls.json_obj_list.append(cls_obj.to_dictionary())

        with open(cls.filename, "w") as file:
            file.write(cls.to_json_string(cls.json_obj_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string:
            return json_string
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        pass
        # att_list = ['width', 'height']
        # for att in att_list:
        #     if att in dictionary:
        #         obj_instance = Rectangle(1, 4)
        #     elif 'size' in dictionary:
        #         obj_instance = Square(5)

        # obj_instance.update(**dictionary)
        # return obj_instance
