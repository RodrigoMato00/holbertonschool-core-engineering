#!/usr/bin/env python3
"""Module defining a Square class with size validation."""


class Square:
    """Square with private size attribute and validation."""

    def __init__(self, size=0):
        """Initialize Square with size (must be int >= 0)."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
