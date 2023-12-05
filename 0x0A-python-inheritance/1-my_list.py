#!/usr/bin/python3


"""This module cntains a class that inherits from list class """


class MyList(list):
    """ This class contains the implementation of sorting a list."""

    def print_sorted(self):
        self.sorted_list = []

        sorted_list = sorted(self)

        print(sorted_list)
