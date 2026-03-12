#!/usr/bin/env python3
import add_0 as a0


def add(a, b):
    """Return a + b."""
    return a + b


if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, a0.add(a, b)))
