#!/usr/bin/env python3
"""Square class inheriting from Rectangle (width == height == size)."""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square: rectangle with width and height equal to size."""

    def __init__(self, size):
        """Initialize square; pass size as width and height to parent."""
        super().__init__(size, size)
