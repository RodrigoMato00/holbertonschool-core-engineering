#!/usr/bin/env python3
"""Test Task 1: concat with type annotations."""
concat = __import__('concat').concat

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)
