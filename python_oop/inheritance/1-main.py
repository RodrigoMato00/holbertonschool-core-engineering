#!/usr/bin/env python3
"""Test Rectangle (inherits BaseGeometry)."""
Rectangle = __import__('1-rectangle').Rectangle

r = Rectangle(3, 5)
print(r)
print(dir(r))
print("width", r._Rectangle__width, "height", r._Rectangle__height)

try:
    r2 = Rectangle(0, 5)
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))

try:
    r3 = Rectangle(3, -1)
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))
