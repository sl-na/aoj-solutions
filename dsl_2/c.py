# Range Search (kD Tree)


import sys


class Node:
    def __init__(self, point, axis, left=None, right=None):
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right


def build_kd_tree(points, depth=0):
    if not points:
        return
    k = len(points[0]) - 1
    axis = depth % k
    points.sort(key=lambda x: x[axis])
    median = len(points) // 2
    point = points[median]
    left = build_kd_tree(points[0:median], depth + 1)
    right = build_kd_tree(points[median + 1 :], depth + 1)
    node = Node(point, axis, left, right)
    return node


def range_search(node, rect, found, depth=0):
    if not node:
        return
    x, y, i = node.point
    sx, tx, sy, ty = rect
    if sx <= x <= tx and sy <= y <= ty:
        found.append(i)
    if node.axis == 0:
        if sx <= x:
            range_search(node.left, rect, found, depth + 1)
        if x <= tx:
            range_search(node.right, rect, found, depth + 1)
    else:
        if sy <= y:
            range_search(node.left, rect, found, depth + 1)
        if y <= ty:
            range_search(node.right, rect, found, depth + 1)


def main():
    it = map(int, sys.stdin.read().split())
    n = next(it)
    points = []
    for i in range(n):
        x, y = next(it), next(it)
        points.append((x, y, i))
    tree = build_kd_tree(points)
    answer = []
    _p = next(it)
    for sx, tx, sy, ty in zip(it, it, it, it):
        found = []
        range_search(tree, (sx, tx, sy, ty), found)
        found.sort()
        for i in found:
            answer.append(f"{i}")
        answer.append("")
    print("\n".join(answer))


if __name__ == "__main__":
    main()
