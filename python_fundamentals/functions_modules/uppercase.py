#!/usr/bin/env python3
def uppercase(str):
    """Print str in uppercase (ASCII ord/chr), then newline. No return."""
    out = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            out += chr(ord(c) - 32)
        else:
            out += c
    print("{}".format(out))
