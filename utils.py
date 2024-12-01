from dataclasses import dataclass

@dataclass(frozen=True)
class Vector2D:
    x: int
    y: int

    def __abs__(self):
        return abs(self.x) + abs(self.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector2D(self.x*other, self.y*other)
        return NotImplemented

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def perp(self):
        return Vector2D(-self.y, self.x)
