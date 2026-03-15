#!/usr/bin/env python3
"""Test Square #2: polymorphism (Rectangle and Square)."""
Rectangle = __import__('2-rectangle').Rectangle
Square = __import__('2-square').Square

shapes = [Rectangle(3, 5), Square(4)]
for shape in shapes:
    print(shape)
    print(shape.area())
