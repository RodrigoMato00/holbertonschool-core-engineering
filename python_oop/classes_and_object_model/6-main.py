#!/usr/bin/env python3
"""Test script for Task 6: Print Square Instance."""
Square = __import__('6-square').Square

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)
