#!/usr/bin/python3
""" Importing json for json-related tasks """
import json
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

    def to_json_string(list_dictionaries):
        """ Converting dictionaries to json strings """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return json.dumps()
        return json.dumps(list_dictionaries)
