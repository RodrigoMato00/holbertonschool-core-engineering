#!/usr/bin/env python3
"""SwimMixin, FlyMixin, and Dragon (mixins)."""


class SwimMixin:
    """Mixin that provides swim behavior."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides fly behavior."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon: swim and fly via mixins; roar method."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
