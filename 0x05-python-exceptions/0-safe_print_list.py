#!/usr/bin/python3

def lis_len(my_list=[]):
    """This function calculates the lenght of a list.

    Args:
        my_list: List whose lenght is to be calculated.

    Returns:
        The lenght of my_list.
    """

    list_len = 0

    for element in my_list:
        list_len += 1

    return (list_len)


def safe_print_list(my_list=[], x=0):
    new_list = []

    num_of_element = 0

    try:
        new_list = my_list[:x]

        for item in new_list:
            print(item, end='')
            
        print()
        num_of_element = lis_len(new_list)

    except Exception as e:
        print()

    return num_of_element
