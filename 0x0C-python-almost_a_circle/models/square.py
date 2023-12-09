#!/usr/bin/python3

"""This module contains a class Square that extends the Rectngle class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This class is defined for the Square clss that extends
       the Rectangle class.
       Atrributes:
           size (int): this represents the size attribute of the Square.
           x (int): this represent the x-cordinate of the Square object.
           y (int): this represents the y-cordinate of the Square object.
           id (int): this reperents the id of the Square object.
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.__size = size

    def __str__(self):
        idx = self.id
        x_c = self.x
        y_c = self.y
        rep = "[Sqaure] ({}) {}/{} - {}".format(idx, x_c, y_c, self.__size)
        return rep

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        return self.width
        # self.height = value
