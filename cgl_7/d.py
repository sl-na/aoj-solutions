# Cross Points of a Circle and a Line

import sys
from dataclasses import dataclass
from math import hypot, sqrt

EPS = 1e-10


def equals(a, b):
    return abs(a - b) < EPS


@dataclass(order=True)
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

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def norm(self):
        return self.dot(self)

    def cross(self, other):
        return self.x * other.y - self.y * other.x


Vector = Point


@dataclass
class Line:
    p1: Point
    p2: Point

    @property
    def vector(self):
        return self.p2 - self.p1


@dataclass
class Segment:
    p1: Point
    p2: Point

    @property
    def vector(self):
        return self.p2 - self.p1


@dataclass
class Circle:
    center: Point
    r: float


@dataclass
class Polygon:
    vertices: list[Point]


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


def project(l, p):
    base = l.vector
    r = (p - l.p1).dot(base) / base.norm()
    return l.p1 + base * r


def reflect(l, p):
    return p + (project(l, p) - p) * 2.0


def is_orthogonal(l1, l2):
    v1 = l1.vector
    v2 = l2.vector
    return equals(v1.dot(v2), 0.0)


def is_parallel(l1, l2):
    v1 = l1.vector
    v2 = l2.vector
    return equals(v1.cross(v2), 0.0)


def intersects(p1, p2, p3, p4):
    return (
        ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0
        and ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0
    )


def intersects_ss(s1, s2):
    return intersects(s1.p1, s1.p2, s2.p1, s2.p2)


def cross_point_ll(l1, l2):
    base = l2.vector
    d1 = abs(base.cross(l1.p1 - l2.p1))
    d2 = abs(base.cross(l1.p2 - l2.p1))
    t = d1 / (d1 + d2)
    return l1.p1 + l1.vector * t


def cross_point_ss(s1, s2):
    if not intersects_ss(s1, s2):
        return
    return cross_point_ll(s1, s2)


def cross_point_cl(c, l):
    pr = project(l, c.center)
    e = l.vector / abs(l.vector)
    base = sqrt(c.r * c.r - (pr - c.center).norm())
    p1 = pr + e * base
    p2 = pr - e * base
    return sorted([p1, p2])


def distance(p1, p2):
    return abs(p1 - p2)


def distance_lp(l, p):
    return abs(l.vector.cross(p - l.p1)) / abs(l.vector)


def distance_sp(s, p):
    if s.vector.dot(p - s.p1) < -EPS:
        return abs(p - s.p1)
    if (s.p1 - s.p2).dot(p - s.p2) < -EPS:
        return abs(p - s.p2)
    return distance_lp(s, p)


def distance_ss(s1, s2):
    if intersects_ss(s1, s2):
        return 0.0
    return min(
        distance_sp(s1, s2.p1),
        distance_sp(s1, s2.p2),
        distance_sp(s2, s1.p1),
        distance_sp(s2, s1.p2),
    )


def main():
    it = map(int, sys.stdin.read().split())
    cx, cy, r = next(it), next(it), next(it)
    circle = Circle(Point(cx, cy), r)
    _ = next(it)
    answer = []
    for lx1, ly1, lx2, ly2 in zip(it, it, it, it):
        p1 = Point(lx1, ly1)
        p2 = Point(lx2, ly2)
        line = Line(p1, p2)
        cp1, cp2 = cross_point_cl(circle, line)
        answer.append(f"{cp1.x:.8f} {cp1.y:.8f} {cp2.x:.8f} {cp2.y:.8f}")
    print("\n".join(answer))


if __name__ == "__main__":
    main()
