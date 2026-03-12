# Exception Handling

try/except, specific exception types, else/finally, raising exceptions.

## Tasks

- **0. Safe list printing** — `safe_print_list.py`: print at most x elements of a list, return count; no exception if x > len(list).
- **1. Safe integer printing** — `safe_print_integer.py`: print value with `{:d}` if int, return True; else return False.
- **2. Safe list printing with type handling** — `safe_print_list_integers.py`: from first x elements, print only integers, skip others; return count.
- **3. Divide two integers safely** — `safe_print_division.py`: divide a/b in try; ZeroDivisionError → "division by 0"; other → "Inside result: None"; finally print "Inside result: &lt;result&gt;"; return result or None.
