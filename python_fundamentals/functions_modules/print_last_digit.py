#!/usr/bin/env python3
def print_last_digit(number):
    """Print last digit (positive) and return it. No extra text."""
    digit = abs(number) % 10
    print("{}".format(digit), end="")
    return digit
