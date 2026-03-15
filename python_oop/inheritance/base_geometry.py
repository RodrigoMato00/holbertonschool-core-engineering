#!/usr/bin/env python3
"""Base class for geometric shapes; area() and integer_validator."""


class BaseGeometry:
    """Base for geometry; subclasses implement area and reuse validator."""

    def area(self):
        """Raise exception: area not implemented in base class."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
