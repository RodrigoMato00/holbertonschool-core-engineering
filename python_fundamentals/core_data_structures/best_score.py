#!/usr/bin/env python3
def best_score(a_dictionary):
    """Return key with biggest integer value; None if dict is None or empty."""
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    return max(a_dictionary, key=a_dictionary.get)
