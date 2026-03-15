#!/usr/bin/env python3
"""Module defining a Square class with private instance attribute size."""


class Square:
    """Square with a private instance attribute size."""

    def __init__(self, size):
        """Initialize Square with size (stored as private attribute)."""
        self.__size = size
