from collections.abc import Iterable, Sequence
from dataclasses import dataclass
import re

def table(input, dtype=None):
    rows = []
    for line in input.splitlines():
        row = line.split()
        if dtype is None:
            rows.append(row)
        else:
            rows.append(list(map(dtype, row)))
    return rows

def ints(s):
    return list(map(int, re.findall(r'[+-]?[0-9]+', s)))

def sliding_window(xs, size):
    if isinstance(xs, Sequence):
        for i in range(len(xs) - size + 1):
            yield xs[i : i + size]
    elif isinstance(xs, Iterable):
        it = iter(xs)
        window = tuple(next(it) for _ in range(size))
        yield window
        for x in it:
            window = window[1:] + (x, )
            yield window

@dataclass(frozen=True, order=True)
class Vector2D:
    x: int
    y: int

    def __abs__(self):
        return abs(self.x) + abs(self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x*other.x, self.y*other.y)
        else:
            return Vector2D(self.x*other, self.y*other)

    def __floordiv__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x//other.x, self.y//other.y)
        else:
            return Vector2D(self.x//other, self.y//other)

    def __mod__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x%other.x, self.y%other.y)
        else:
            return Vector2D(self.x%other, self.y%other)

    def rot90(self, n=1):
        # y axis points downwards -> clockwise
        # y axis points upwards -> anticlockwise
        match n % 4:
            case 0:
                return self
            case 1:
                return Vector2D(-self.y, self.x)
            case 2:
                return Vector2D(-self.x, -self.y)
            case 3:
                return Vector2D(self.y, -self.x)

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def cross(self, other):
        return self.x*other.y - self.y*other.x

    @staticmethod
    def parse(s, sep=','):
        return Vector2D(*map(int, s.split(sep)))

    def __str__(self):
        return ','.join((str(self.x), str(self.y)))
