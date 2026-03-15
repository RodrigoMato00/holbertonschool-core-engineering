#!/usr/bin/env python3
"""Test Task 0: add with type annotations."""
add = __import__('add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
