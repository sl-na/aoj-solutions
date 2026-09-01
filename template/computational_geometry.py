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


Polygon = list[Point]


@dataclass
class EndPoint:
    p: Point
    seg: int
    st: int

    def __lt__(self, other):
        if self.p.y == other.p.y:
            return self.st < other.st
        else:
            return self.p.y < other.p.y


class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i, x):
        while i <= self.n:
            self.tree[i] += x
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def query(self, l, r):
        if l > r:
            return 0
        return self.sum(r) - self.sum(l - 1)


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
    d1 = base.cross(l1.p1 - l2.p1)
    d2 = base.cross(l1.p2 - l2.p1)
    if equals(d2, 0.0):
        return None
    t = -d1 / d2
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


IN = 2
ON = 1
OUT = 0

POINT_CONTAIN_NAMES = {IN: "IN", ON: "ON", OUT: "OUT"}


def contains(polygon, point):
    n = len(polygon)
    is_inside = False
    for i in range(n):
        a = polygon[i] - point
        b = polygon[(i + 1) % n] - point
        if abs(a.cross(b)) < EPS and a.dot(b) < EPS:
            return ON
        if a.y > b.y:
            a, b = b, a
        if a.y < EPS < b.y and a.cross(b) > EPS:
            is_inside = not is_inside
    return IN if is_inside else OUT


def andrew_scan(polygon):
    if len(polygon) < 3:
        return polygon
    sorted_polygon = sorted(polygon)
    lower = Polygon()
    for p in sorted_polygon:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) == CLOCKWISE:
            lower.pop()
        lower.append(p)
    upper = Polygon()
    for p in reversed(sorted_polygon):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) == CLOCKWISE:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


BOTTOM = 0
LEFT = 1
RIGHT = 2
TOP = 3


def manhattan_intersection(segments):
    endpoints = []
    x_coords = set()
    for i, s in enumerate(segments):
        if s.p1.y == s.p2.y:
            if s.p1.x > s.p2.x:
                s.p1, s.p2 = s.p2, s.p1
            endpoints.append(EndPoint(s.p1, i, LEFT))
            endpoints.append(EndPoint(s.p2, i, RIGHT))
        else:
            if s.p1.y > s.p2.y:
                s.p1, s.p2 = s.p2, s.p1
            endpoints.append(EndPoint(s.p1, i, BOTTOM))
            endpoints.append(EndPoint(s.p2, i, TOP))
        x_coords.add(s.p1.x)
        x_coords.add(s.p2.x)
    endpoints.sort()
    sorted_x = sorted(x_coords)
    x_to_idx = {x: i + 1 for i, x in enumerate(sorted_x)}
    bit = BIT(len(sorted_x))
    cnt = 0
    for ep in endpoints:
        if ep.st == TOP:
            bit.add(x_to_idx[ep.p.x], -1)
        elif ep.st == BOTTOM:
            bit.add(x_to_idx[ep.p.x], 1)
        elif ep.st == LEFT:
            x1 = segments[ep.seg].p1.x
            x2 = segments[ep.seg].p2.x
            l = x_to_idx[x1]
            r = x_to_idx[x2]
            cnt += bit.query(l, r)
    return cnt
