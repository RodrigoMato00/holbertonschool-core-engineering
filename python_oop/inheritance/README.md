# Inheritance & Polymorphism

Class hierarchy: BaseGeometry → Rectangle → Square. Reuse and override behavior; polymorphism.

## Tasks

- **0. Base Geometry** — `base_geometry.py`: Class `BaseGeometry` with `area()` (raises Exception) and `integer_validator(name, value)` (int, > 0).
- **1. Rectangle** — `1-rectangle.py`: Class `Rectangle(BaseGeometry)` with width and height validated via `integer_validator`.
- **2. Full Rectangle** — `2-rectangle.py`: Rectangle with `area()` and `__str__()` (readable representation).
- **3. Square #1** — `1-square.py`: Class `Square(Rectangle)`; constructor receives `size`, initializes parent with `(size, size)`.
