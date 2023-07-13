#!/usr/bin/python3

class BaseGeometry:
    """A base geometry class"""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the value to be an integer and greater than 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiates a Rectangle object with width and height"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string representation of the Rectangle object"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Computes and returns the area of the Rectangle"""
        return self.__width * self.__height
