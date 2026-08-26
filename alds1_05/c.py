# Koch Curve


from math import cos, pi, sin


class Point:
    x: float
    y: float

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


def draw_koch_curve(d, p1, p2):
    if d == 0:
        return
    s = Point()
    t = Point()
    u = Point()
    th = pi * 60.0 / 180.0
    s.x = (2.0 * p1.x + 1.0 * p2.x) / 3.0
    s.y = (2.0 * p1.y + 1.0 * p2.y) / 3.0
    t.x = (1.0 * p1.x + 2.0 * p2.x) / 3.0
    t.y = (1.0 * p1.y + 2.0 * p2.y) / 3.0
    u.x = (t.x - s.x) * cos(th) - (t.y - s.y) * sin(th) + s.x
    u.y = (t.x - s.x) * sin(th) + (t.y - s.y) * cos(th) + s.y
    draw_koch_curve(d - 1, p1, s)
    print(f"{s.x:.8f} {s.y:.8f}")
    draw_koch_curve(d - 1, s, u)
    print(f"{u.x:.8f} {u.y:.8f}")
    draw_koch_curve(d - 1, u, t)
    print(f"{t.x:.8f} {t.y:.8f}")
    draw_koch_curve(d - 1, t, p2)


def main():
    n = int(input())
    p1 = Point()
    p2 = Point(100.0)
    print(f"{p1.x:.8f} {p1.y:.8f}")
    draw_koch_curve(n, p1, p2)
    print(f"{p2.x:.8f} {p2.y:.8f}")


if __name__ == "__main__":
    main()
