#!/usr/bin/env python3
"""Rectangle class with private width and height, getters and setters."""


class Rectangle:
    """Rectangle with private width and height (int >= 0)."""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle with optional width and height (default 0)."""
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the current width (getter)."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width (must be int >= 0)."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the current height (getter)."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height (must be int >= 0)."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
