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
