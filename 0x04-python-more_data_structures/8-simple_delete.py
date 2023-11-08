#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    if key:
        for dict_key in a_dictionary.keys():
            if dict_key == key:
                del(dict_key)

    return a_dictionary
