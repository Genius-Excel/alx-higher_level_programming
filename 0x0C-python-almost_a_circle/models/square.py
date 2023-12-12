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
        """square repr"""
        idx = self.id
        x_c = self.x
        y_c = self.y
        rep = "[Square] ({}) {}/{} - {}".format(idx, x_c, y_c, self.__size)
        return rep

    # @Rectangle.width.getter
    @property
    def size(self):
        """size getter property"""
        return self.__width

    @Rectangle.width.setter
    # @size.setter
    def size(self, value):
        """size setter property"""
        self.__width = value
        # Rectangle.width.fset(self, value)
        # self.height = value

    def update(self, *args, **kwargs):
        """update method"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.__size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """object dictionary"""
        sq_dict = {
            'id': self.id,
            'size': self.__size,
            'x': self.x,
            'y': self.y
        }

        return sq_dict
