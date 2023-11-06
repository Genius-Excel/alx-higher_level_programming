#!/usr/bin/python3

def no_c(my_string):
    new_string = []

#    str_list = list(my_string)

    for char in my_string:

        if char not in "cC":
            new_string.append(char)

#    new_string = str(new_string)

    return "".join(new_string)
