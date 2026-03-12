#!/usr/bin/env python3
def safe_print_list_integers(my_list=[], x=0):
    """Print ints from first x elements, skip others. Return count."""
    count = 0
    n = min(x, len(my_list))
    for i in range(n):
        if isinstance(my_list[i], int):
            print("{:d}".format(my_list[i]), end="")
            count += 1
    print()
    return count
