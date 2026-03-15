#!/usr/bin/env python3
"""Abstract Shape and concrete Circle, Rectangle; shape_info (duck typing)."""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base; subclasses implement area() and perimeter()."""

    @abstractmethod
    def area(self):
        """Return area (implemented by subclasses)."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return perimeter (implemented by subclasses)."""
        pass


class Circle(Shape):
    """Circle with given radius."""

    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Return pi * radius^2."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return 2 * pi * radius (circumference)."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle with width and height."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return width * height."""
        return self.width * self.height

    def perimeter(self):
        """Return 2 * (width + height)."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of shape (duck typing: no isinstance)."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
