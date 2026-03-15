#!/usr/bin/env python3
"""Fish, Bird, and FlyingFish (multiple inheritance)."""


class Fish:
    """Fish: swim and habitat."""

    def swim(self):
        """Print that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print that the fish lives in water."""
        print("The fish lives in water")


class Bird:
    """Bird: fly and habitat."""

    def fly(self):
        """Print that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print that the bird lives in the sky."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish: inherits Fish and Bird; overrides fly, swim, habitat."""

    def fly(self):
        """Print that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print that the flying fish lives in water and sky."""
        print("The flying fish lives both in water and the sky!")
