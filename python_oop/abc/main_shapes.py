#!/usr/bin/env python3
"""Test Task 1: shape_info with Circle and Rectangle."""
from shapes import Circle, Rectangle, shape_info

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)
