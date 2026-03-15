#!/usr/bin/env python3
"""Test Task 5: User class annotations."""
User = __import__('user').User

user = User("Alice", 30)
print(user.name)
print(user.age)
