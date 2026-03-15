#!/usr/bin/env python3
"""Rectangle class inheriting from BaseGeometry; width and height validated."""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle defined by width and height (validated via parent)."""

    def __init__(self, width, height):
        """Init rectangle; validate width and height via parent validator."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
