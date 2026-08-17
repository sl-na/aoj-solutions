# Parallel/Orthogonal

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

    def __truediv__(self, scalar):
        return type(self)(self.x / scalar, self.y / scalar)

    def __abs__(self):
        return sqrt(self.norm())

    def __lt__(self, other):
        if abs(self.x - other.x) > EPS:
            return self.x < other.x
        return self.y < other.y

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


class Point(Vector):
    pass


class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"Segment({self.p1}, {self.p2})"

    @property
    def vector(self):
        return self.p2 - self.p1

    def is_orthogonal(self, other):
        return abs(self.vector.dot(other.vector)) < EPS

    def is_parallel(self, other):
        return abs(self.vector.cross(other.vector)) < EPS


def main():
    it = map(int, sys.stdin.read().split())
    _ = next(it)
    answer = []
    for xp0, yp0, xp1, yp1, xp2, yp2, xp3, yp3 in zip(*[it] * 8):
        s1 = Segment(Point(xp0, yp0), Point(xp1, yp1))
        s2 = Segment(Point(xp2, yp2), Point(xp3, yp3))
        if s1.is_parallel(s2):
            answer.append("2")
        elif s1.is_orthogonal(s2):
            answer.append("1")
        else:
            answer.append("0")
    print("\n".join(answer))


if __name__ == "__main__":
    main()
