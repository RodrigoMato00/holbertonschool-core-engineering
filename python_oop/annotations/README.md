# Type Annotations

Type hints for parameters, return values, variables, containers, and classes; mypy.

## Tasks

- **0. Basic annotations - add** — `add.py`: Function `add(a: float, b: float) -> float` returning `a + b`.
- **1. Basic annotations - concat** — `concat.py`: Function `concat(str1: str, str2: str) -> str` returning concatenated string.
- **2. Basic annotations - floor** — `floor.py`: Function `floor(n: float) -> int` returning floor of n (math.floor).
- **3. Define variables** — `define_variables.py`: Annotated variables `a: int = 1`, `pi: float = 3.14`, `i_understand_annotations: bool = True`, `school: str = "Holberton"`.
- **4. Complex types - list of floats** — `sum_list.py`: Function `sum_list(input_list: List[float]) -> float` (typing.List).
- **5. Class annotations** — `user.py`: Class `User` with annotated attributes `name: str`, `age: int`; constructor initializes from parameters.
- **6. Static type checking** — `type_check.py`: `zoom_array(lst: Tuple, factor: int = 2) -> List`; mypy-validated; `array` as tuple, `factor` int (e.g. 3).
