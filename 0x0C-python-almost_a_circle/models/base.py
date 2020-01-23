#!/usr/bin/python3
""" Base.py """


class Base():
    """ Base class. Handles id of future classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization function """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
