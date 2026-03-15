#!/usr/bin/env python3
"""Square with custom __str__ (readable representation)."""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square: rectangle with width == height; __str__ returns [Square] w/h."""

    def __init__(self, size):
        """Initialize square; pass size as width and height to parent."""
        super().__init__(size, size)

    def __str__(self):
        """Return readable string: [Square] width/height."""
        w, h = self._Rectangle__width, self._Rectangle__height
        return "[Square] {}/{}".format(w, h)
