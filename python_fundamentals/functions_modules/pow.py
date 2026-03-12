#!/usr/bin/env python3
def pow(a, b):
    """Return a ** b. No ** operator, no imports, use a loop."""
    if b == 0:
        return 1
    exp = b if b > 0 else -b
    result = 1
    for _ in range(exp):
        result *= a
    if b < 0:
        return 1 / result
    return result
