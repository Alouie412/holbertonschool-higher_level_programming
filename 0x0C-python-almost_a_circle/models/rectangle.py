#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        Rectangle.set_width(self, width)
        Rectangle.set_height(self, height)
        Rectangle.set_x(self, x)
        Rectangle.set_y(self, y)

    def get_width(self):
        return self.__width

    def set_width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def get_height(self):
        return self.__height

    def set_height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def get_x(self):
        return self.__x

    def set_x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def get_y(self):
        return self.__y

    def set_y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(0, self.__height):
            print("#" * self.__width)

    def __str__(self):
        return ("[{}] ({}) {}/{} - {}/{}".format("Rectangle", self.id, self.__x, self.__y, self.__width, self.__height))