# Cross Points of Circles

import sys
from dataclasses import dataclass
from math import acos, atan2, cos, hypot, sin, sqrt

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

    def angle(self):
        return atan2(self.y, self.x)


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


def polar(r, a):
    return Point(r * cos(a), r * sin(a))


def cross_point_cc(c1, c2):
    d = abs(c1.center - c2.center)
    a = acos((c1.r * c1.r + d * d - c2.r * c2.r) / (2 * c1.r * d))
    t = (c2.center - c1.center).angle()
    cp1 = c1.center + polar(c1.r, t + a)
    cp2 = c1.center + polar(c1.r, t - a)
    return sorted([cp1, cp2])


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
    c1x, c1y, c1r = next(it), next(it), next(it)
    c2x, c2y, c2r = next(it), next(it), next(it)
    c1 = Circle(Point(c1x, c1y), c1r)
    c2 = Circle(Point(c2x, c2y), c2r)
    p1, p2 = cross_point_cc(c1, c2)
    print(f"{p1.x:.6f} {p1.y:.6f} {p2.x:.6f} {p2.y:.6f}")


if __name__ == "__main__":
    main()
