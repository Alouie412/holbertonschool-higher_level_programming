#!/usr/bin/python3
""" Unittest for the Rectangle class.
To ensure Rectangle is working as intended """

import unittest
import json
from models import base
from models.base import Base
from models.rectangle import Rectangle


class RectangleTesting(unittest.TestCase):
    """ Test cases for the Rectangle class """

    def setUp(cls):
        """ Resets object to 0. For id """
        Base._Base__nb_objects = 0

    def test_rec(self):
        """ Test for valid rectangle """
        rec = Rectangle(1, 5)
        self.assertEqual(type(r.width), int)
        self.assertEqual(type(r.height), int)
        self.assertEqual((rec.width, rec.height, rec.x, rec.y, id),
                         (1, 5, 0, 0, 1))
        rec = Rectangle(3, 3, 1)
        self.assertEqual((rec.width, rec.height, rec.x, rec.y, id),
                        (3, 3, 1, 0, 2))
        with self.assertRaises(TypeError):
            rec = Rectangle("Potato", 1)
        with self.assertRaises(ValueError):
            rec = Rectangle(5, -99)

    def test_area(self):
        """ Test for correct area calculation """
        rec = Rectangle(5, 5)
        self.assertEqual(rec.area(), 25)
        rec = Rectangle(6, 11, 2, 7, 32767)
        self.assertEqual(rec.area(), 66)

    def display_rec_info(self):
        """ Test for proper text display """
        rec = Rectangle(3, 2, 7, 6, 7)
        line = "[Rectangle] ({}) {}/{} - {}/{}"
        .format(rec.id, rec.x, rec.y, rec.width, rec.height)
        self.assertEqual(str(rec), line)

    def updater(self):
        """ Test for correct modification to rectangle stats """
        rec = Rectangle(1, 1, 1, 1)
        rec.update(5)
        line = "[Rectangle] ({}) {}/{} - {}/{}"
        .format(rec.id, rec.x, rec.y, rec.width, rec.height)
        self.assertEqual(str(rec), line)
        rec.update(5, 2, 2)
        self.assertEqual(str(rec), line)
        rec = Rectangle(1, 1, 1, 1)
        rec.update(height=5)
        self.assertEqual(str(rec), line)
        rec.update(x=6, width=7, id=999)
        self.assertEqual(str(rec), line)


if __name__ == '__main__':
    unittest.main()
