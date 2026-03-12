#!/usr/bin/env python3
def safe_print_list(my_list=[], x=0):
    """Print at most x elements of my_list. Return number actually printed."""
    count = 0
    n = min(x, len(my_list))
    for i in range(n):
        print(my_list[i], end="")
        count += 1
    print()
    return count
