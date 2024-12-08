from collections.abc import Iterable, Sequence
from dataclasses import dataclass

def table(input, dtype=None):
    rows = []
    for line in input.splitlines():
        row = line.split()
        if dtype is None:
            rows.append(row)
        else:
            rows.append(list(map(dtype, row)))
    return rows

def sliding_window(xs, size):
    if isinstance(xs, Sequence):
        for i in range(len(xs) - size + 1):
            yield xs[i : i + size]
    else:
        it = iter(xs)
        window = tuple(next(it) for _ in range(size))
        yield window
        for x in it:
            window = window[1:] + (x, )
            yield window

@dataclass(frozen=True)
class Vector:
    x: int
    y: int

    def __abs__(self):
        return abs(self.x) + abs(self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, n):
        return Vector(self.x*n, self.y*n)
