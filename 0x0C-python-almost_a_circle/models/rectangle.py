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
            width (int): this represents the width of the Rectangle
                        object as a private instance attribute.
            height (int): this represents the height of the Rectangle
                        object as a private intance attibute.
            x (int): this represent the x co-ordinate postion of the
                        Rectangle object as a private attribute.
            y (int): this represent the y co-ordinate postion of the
                    Rectangle object as a private attribute.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id=id)
        # validate the width attribute.
        if not isinstance(width, int):
            raise TypeError("width must be an intger")
        elif width <= 0:
            raise ValueError("width must be > 0")

        # validate the height attribute
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")

        # validate x-cordinate attribute
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")

        # validae the y-cordinate attribute
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        rp = "[Rectangle] ({}) {}/{} - {}/{}\
            ".format(self.id, self.__x, self.__y, self.__width, self.__height)
        return rp

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        return (self.width * self.height)

    def display(self):
        output = ('\n' * self.__y)

        for i in range(self.__height):
            output += ' ' * self.__x + '#' * self.__width + '\n'

        print(output, end='')

    def update(self, *args, **kwargs):
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]

        if not args:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        rect_dict = {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }

        return rect_dict
