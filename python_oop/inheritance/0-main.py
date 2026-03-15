#!/usr/bin/env python3
"""Test BaseGeometry: area() and integer_validator."""
BaseGeometry = __import__('base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))
