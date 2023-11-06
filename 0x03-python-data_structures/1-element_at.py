#!/usr/bin/python3
def element_at(my_list, idx):
    element = None

    list_len = len(my_list)

    if idx >= list_len or idx < 0:
        return None

    element = my_list[idx]

    return element
