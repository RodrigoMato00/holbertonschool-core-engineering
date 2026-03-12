#!/usr/bin/env python3
def safe_print_division(a, b):
    """Divide a by b; print result in finally. Return result or None."""
    result = None
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
