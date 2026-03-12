#!/usr/bin/env python3
def safe_print_integer(value):
    """Print value with {:d} if it's an int; return True, else return False."""
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
