# Counter-Clockwise

import sys
from dataclasses import dataclass
from math import hypot

EPS = 1e-10


def equals(a, b):
    return abs(a - b) < EPS


@dataclass(order=True, frozen=True)
class Point:
    x: float
    y: float

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return Point(self.x / scalar, self.y / scalar)

    def __abs__(self):
        return hypot(self.x, self.y)

    def norm(self):
        return self.x**2 + self.y**2

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x


Vector = Point

COUNTER_CLOCKWISE = 1
CLOCKWISE = -1
ONLINE_BACK = 2
ONLINE_FRONT = -2
ON_SEGMENT = 0

CCW_RESULT_NAMES = {
    COUNTER_CLOCKWISE: "COUNTER_CLOCKWISE",
    CLOCKWISE: "CLOCKWISE",
    ONLINE_BACK: "ONLINE_BACK",
    ONLINE_FRONT: "ONLINE_FRONT",
    ON_SEGMENT: "ON_SEGMENT",
}


def ccw(p0, p1, p2):
    a = p1 - p0
    b = p2 - p0
    cross_val = a.cross(b)
    if cross_val > EPS:
        return COUNTER_CLOCKWISE
    if cross_val < -EPS:
        return CLOCKWISE
    if a.dot(b) < -EPS:
        return ONLINE_BACK
    if a.norm() < b.norm() - EPS:
        return ONLINE_FRONT
    return ON_SEGMENT


@dataclass
class Segment:
    p1: Point
    p2: Point

    @property
    def vector(self):
        return self.p2 - self.p1

    def project(self, p):
        base = self.vector
        r = base.dot(p - self.p1) / base.norm()
        return self.p1 + base * r

    def reflect(self, p):
        return p + (self.project(p) - p) * 2.0

    def is_orthogonal(self, other):
        return equals(self.vector.dot(other.vector), 0.0)

    def is_parallel(self, other):
        return equals(self.vector.cross(other.vector), 0.0)

    def intersects(self, other):
        return (
            ccw(self.p1, self.p2, other.p1) * ccw(self.p1, self.p2, other.p2) <= 0
            and ccw(other.p1, other.p2, self.p1) * ccw(other.p1, other.p2, self.p2) <= 0
        )

    def distance_to_line(self, p):
        return abs(self.vector.cross(p - self.p1)) / abs(self.vector)

    def distance_to_point(self, p):
        if self.vector.dot(p - self.p1) < 0.0:
            return abs(p - self.p1)
        if (self.p1 - self.p2).dot(p - self.p2) < 0.0:
            return abs(p - self.p2)
        return self.distance_to_line(p)

    def distance_to_segment(self, other):
        if self.intersects(other):
            return 0.0
        return min(
            self.distance_to_point(other.p1),
            self.distance_to_point(other.p2),
            other.distance_to_point(self.p1),
            other.distance_to_point(self.p2),
        )


def main():
    it = map(int, sys.stdin.read().split())
    xp0, yp0, xp1, yp1 = next(it), next(it), next(it), next(it)
    p0 = Point(xp0, yp0)
    p1 = Point(xp1, yp1)
    _ = next(it)
    answer = []
    for xp2, yp2 in zip(it, it):
        p2 = Point(xp2, yp2)
        result = ccw(p0, p1, p2)
        answer.append(CCW_RESULT_NAMES[result])
    print("\n".join(answer))


if __name__ == "__main__":
    main()
