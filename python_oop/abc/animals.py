#!/usr/bin/env python3
"""Abstract Animal and concrete subclasses Dog and Cat."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class; subclasses must implement sound()."""

    @abstractmethod
    def sound(self):
        """Return the animal's sound (implemented by subclasses)."""
        pass


class Dog(Animal):
    """Dog: concrete Animal with sound 'Bark'."""

    def sound(self):
        """Return 'Bark'."""
        return "Bark"


class Cat(Animal):
    """Cat: concrete Animal with sound 'Meow'."""

    def sound(self):
        """Return 'Meow'."""
        return "Meow"
