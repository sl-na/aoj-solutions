# Binary Trees


from sys import stdin

NIL = -1


class Node:
    def __init__(self):
        self.parent = NIL
        self.left = NIL
        self.right = NIL


def set_depth(bt: list[Node], index, depths, parent):
    if index == NIL:
        return
    depths[index] = parent
    set_depth(bt, bt[index].left, depths, parent + 1)
    set_depth(bt, bt[index].right, depths, parent + 1)


def set_height(bt: list[Node], index, heights):
    h1 = h2 = 0
    if bt[index].right != NIL:
        h1 = set_height(bt, bt[index].right, heights) + 1
    if bt[index].left != NIL:
        h2 = set_height(bt, bt[index].left, heights) + 1
    heights[index] = max(h1, h2)
    return heights[index]


def get_sibling(bt: list[Node], index):
    if bt[index].parent == NIL:
        return NIL
    if bt[bt[index].parent].left != index and bt[bt[index].parent].left != NIL:
        return bt[bt[index].parent].left
    if bt[bt[index].parent].right != index and bt[bt[index].parent].right != NIL:
        return bt[bt[index].parent].right
    return NIL


def main():
    n = int(stdin.readline())
    inputs = stdin.readlines()
    bt = [Node() for _ in range(n)]
    depths = [0] * n
    heights = [0] * n
    for i in inputs:
        input = list(map(int, i.split()))
        id = input[0]
        left = input[1]
        right = input[2]
        bt[id].left = left
        bt[id].right = right
        if left != NIL:
            bt[left].parent = id
        if right != NIL:
            bt[right].parent = id
    for index, node in enumerate(bt):
        if node.parent == NIL:
            root = index
    set_depth(bt, root, depths, 0)
    set_height(bt, root, heights)
    for i in range(n):
        type = "internal node"
        if bt[i].parent == NIL:
            type = "root"
        elif bt[i].left == NIL and bt[i].right == NIL:
            type = "leaf"
        sibling = get_sibling(bt, i)
        degree = 0
        if bt[i].left != NIL:
            degree += 1
        if bt[i].right != NIL:
            degree += 1
        print(
            f"node {i}: parent = {bt[i].parent}, sibling = {sibling}, degree = {degree}, depth = {depths[i]}, height = {heights[i]}, {type}"
        )


if __name__ == "__main__":
    main()
