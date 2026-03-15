#!/usr/bin/env python3
"""Module defining a Square class with size getter/setter and area method."""


class Square:
    """Square with private size, getter/setter validation, and area method."""

    def __init__(self, size=0):
        """Initialize Square with size (must be int >= 0)."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Return the current size (getter)."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with same validation as __init__ (setter)."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area (side * side)."""
        return self.__size ** 2
