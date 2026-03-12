#!/usr/bin/env python3
def islower(c):
    if not isinstance(c, str) or len(c) != 1:
        return False
    return 97 <= ord(c) <= 122
