#!/usr/bin/env python3
"""Rectangle with area() and __str__ (readable representation)."""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle with width, height; area and string representation."""

    def __init__(self, width, height):
        """Init rectangle; validate width and height via parent validator."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the rectangle area (width * height)."""
        return self.__width * self.__height

    def __str__(self):
        """Return readable string: [Rectangle] width/height."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
