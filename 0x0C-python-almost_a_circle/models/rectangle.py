#!/usr/bin/python3

"""This module contains a class defintion of the Base models class
   This module also contains a class Rectanlge that extends the Base class
"""


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


class Rectangle(Base):
    """This class represents the Rectangle class that extends the base
       class.

        Attributes:
            __width (int): this represents the width of the Rectangle
                        object as a private instance attribute.
            __height (int): this represents the height of the Rectangle
                        object as a private intance attibute.
            __x (int): this represent the x co-ordinate postion of the
                        Rectangle object as a private attribute.
            __y (int): this represent the y co-ordinate postion of the
                    Rectangle object as a private attribute.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id=id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))
