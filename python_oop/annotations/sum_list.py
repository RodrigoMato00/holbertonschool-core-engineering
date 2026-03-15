#!/usr/bin/env python3
"""Type-annotated function sum_list(input_list: List[float]) -> float."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of the floats in input_list."""
    return sum(input_list)
