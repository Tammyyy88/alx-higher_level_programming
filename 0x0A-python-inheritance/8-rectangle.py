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
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def __str__(self):
        """Returns a string representation of the Rectangle object"""
        return f"[Rectangle] {self.__width}/{self.__height}"
