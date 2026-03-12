#!/usr/bin/env python3
def islower(c):
    try:
        if len(c) != 1:
            return False
        return 97 <= ord(c) <= 122
    except (TypeError, AttributeError):
        return False
