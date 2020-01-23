#!/usr/bin/python3
""" This file imports the code found in /models/rectangle.py """
from models.rectangle import Rectangle
""" Square class """


class Square(Rectangle):
    """ Square class. Imports the Rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization """
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size
        self.x = x
        self.y = y

    def __str__(self):
        """ str() function, overloaded """
        return ("[{}] ({}) {}/{} - {}".format("Square", self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        """ Size getter function """
        return self.width

    @size.setter
    def size(self, value):
        """ Size setter function """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = self.width
