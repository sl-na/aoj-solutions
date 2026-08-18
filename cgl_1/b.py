# Reflection

import sys
from math import sqrt

EPS = 1e-10


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return type(self)(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return type(self)(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        return type(self)(self.x / scalar, self.y / scalar)

    def __abs__(self):
        return sqrt(self.norm())

    def __lt__(self, other):
        if abs(self.x - other.x) > EPS:
            return self.x < other.x
        if abs(self.y - other.y) > EPS:
            return self.y < other.y
        return False

    def __eq__(self, other):
        return abs(self.x - other.x) < EPS and abs(self.y - other.y) < EPS

    def __repr__(self):
        return f"{type(self).__name__}({self.x}, {self.y})"

    def norm(self):
        return self.x * self.x + self.y * self.y

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x


Point = Vector


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    @property
    def vec(self):
        return self.p2 - self.p1

    def project(self, p):
        base = self.vec
        norm = base.norm()
        if norm < EPS * EPS:
            return self.p1
        ratio = (p - self.p1).dot(base) / norm
        return self.p1 + base * ratio

    def reflect(self, p):
        return self.project(p) * 2.0 - p

    def is_orthogonal(self, other):
        return abs(self.vec.dot(other.vec)) < EPS

    def is_parallel(self, other):
        return abs(self.vec.cross(other.vec)) < EPS


def main():
    it = map(int, sys.stdin.read().split())
    xp1, yp1, xp2, yp2 = next(it), next(it), next(it), next(it)
    line = Line(Point(xp1, yp1), Point(xp2, yp2))
    _ = next(it)
    answer = []
    for xp, yp in zip(it, it):
        reflected_p = line.reflect(Point(xp, yp))
        answer.append(f"{reflected_p.x:.10f} {reflected_p.y:.10f}")
    print("\n".join(answer))


if __name__ == "__main__":
    main()
