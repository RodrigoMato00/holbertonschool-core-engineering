#!/usr/bin/env python3
"""Square class with size getter/setter, area, and my_print."""


class Square:
    """Square with private size, getter/setter, area, and my_print."""

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

    def my_print(self):
        """Print the square with #; if size is 0, print an empty line."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
