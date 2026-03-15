#!/usr/bin/env python3
"""VerboseList: list subclass that prints on append, extend, remove, pop."""


class VerboseList(list):
    """List that prints a message on append, extend, remove, and pop."""

    def append(self, item):
        """Add item then print notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend list then print how many items were added."""
        n_before = len(self)
        super().extend(iterable)
        n_added = len(self) - n_before
        print("Extended the list with [{}] items.".format(n_added))

    def remove(self, item):
        """Print notification then remove first occurrence of item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Print notification then pop and return item at index."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
