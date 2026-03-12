#!/usr/bin/env python3
def islower(c):
    """True if c is lowercase letter (ASCII), else False. Uses ord()."""
    if len(c) != 1:
        return False
    return 97 <= ord(c) <= 122
