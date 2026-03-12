#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    """Print matrix (list of lists), one row per line, space-sep."""
    for row in matrix:
        print(" ".join("{:d}".format(n) for n in row))
