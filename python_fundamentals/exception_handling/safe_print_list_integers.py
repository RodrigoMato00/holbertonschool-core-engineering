#!/usr/bin/env python3
def safe_print_list_integers(my_list=[], x=0):
    """Print ints from first x elements, skip others. Return count."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
        except (TypeError, ValueError):
            pass
    print()
    return count
