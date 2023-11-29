#!/usr/bin/python3

"""This module contains a class"""


class LockedClass(object):
    """This class is locked, it does not accept dynamically created attr"""

    __slots__ = ('first_name')

    def __init__(self, first_name=None):
        self.first_name = first_name
