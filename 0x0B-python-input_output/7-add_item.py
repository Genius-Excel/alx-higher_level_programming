#!/usr/bin/python3

"""This module contains a function that saves commmand line
   arguments to a JSON object file.
"""

import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_arguments(json_file, *args):
    """This function saves the command line arguments in a JSON file
       Args:
           json_file (any): this represents the JSON file.
           *args (any): this represnts the command line arguments to serialied
    """

    command_line_list = list(args)

    try:
        obj_list = load_from_json_file(json_file)
    except FileNotFoundError:
        obj_list = []  # list is set to be empty if file wasn't created.

    file_obj_list = obj_list + command_line_list

    save_to_json_file(file_obj_list, json_file)


command_args = sys.argv[1:]
json_filename = "add_item.json"

add_arguments(json_filename, *command_args)
