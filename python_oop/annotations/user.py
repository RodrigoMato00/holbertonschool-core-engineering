#!/usr/bin/env python3
"""Type-annotated class User with name and age."""


class User:
    """Simple user with name (str) and age (int)."""

    name: str
    age: int

    def __init__(self, name: str, age: int):
        """Initialize name and age from constructor parameters."""
        self.name = name
        self.age = age
