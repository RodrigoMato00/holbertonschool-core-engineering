#!/usr/bin/env python3
"""Square with size, position, and __str__ (like my_print with offset)."""


class Square:
    """Square with size, position (x, y), and __str__ representation."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square with size and optional position (x, y)."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(p, int) and p >= 0 for p in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """Return the current position (getter)."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position (tuple of 2 positive integers)."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area (side * side)."""
        return self.__size ** 2

    def my_print(self):
        """Print square with # and position; if size 0, print empty line."""
        if self.__size == 0:
            print()
            return
        x, y = self.__position[0], self.__position[1]
        print("\n" * y, end="")
        for _ in range(self.__size):
            print(" " * x + "#" * self.__size)

    def __str__(self):
        """Return string representation (like my_print with position)."""
        if self.__size == 0:
            return "\n"
        x, y = self.__position[0], self.__position[1]
        s = "\n" * y
        for i in range(self.__size):
            s += " " * x + "#" * self.__size
            if i < self.__size - 1:
                s += "\n"
        return s
