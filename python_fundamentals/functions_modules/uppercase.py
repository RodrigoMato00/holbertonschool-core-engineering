#!/usr/bin/env python3
def uppercase(str):
    """Print str in uppercase (ASCII ord/chr), then newline. No return."""
    for c in str:
        if 97 <= ord(c) <= 122:
            print(chr(ord(c) - 32), end="")
        else:
            print(c, end="")
    print()
