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
    x, y, idx = node.point
    sx, tx, sy, ty = rect
    if sx <= x <= tx and sy <= y <= ty:
        found.append(idx)
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
    for idx in range(n):
        x, y = next(it), next(it)
        points.append((x, y, idx))
    tree = build_kd_tree(points)
    answer = []
    q = next(it)
    for _ in range(q):
        sx, tx, sy, ty = next(it), next(it), next(it), next(it)
        found = []
        range_search(tree, (sx, tx, sy, ty), found)
        found.sort()
        for idx in found:
            answer.append(f"{idx}")
        answer.append("")
    print("\n".join(answer))


if __name__ == "__main__":
    main()
