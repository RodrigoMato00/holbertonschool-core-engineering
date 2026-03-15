#!/usr/bin/env python3
"""Test Square (inherits Rectangle)."""
Square = __import__('1-square').Square

s = Square(5)
print(s)
print(s.area())
