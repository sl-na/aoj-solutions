# Rooted Trees


from dataclasses import dataclass
from sys import stdin

NIL = -1


@dataclass
class Node:
    parent: int
    left: int
    right: list[int]


def set_depth(cl, node, depths, parent):
    depths[node] = parent
    if cl[node].right != [NIL]:
        for right in cl[node].right:
            set_depth(cl, right, depths, parent + 1)
    if cl[node].left != NIL:
        set_depth(cl, cl[node].left, depths, parent + 1)


def main():
    n = int(stdin.readline())
    inputs = stdin.readlines()
    cl = [Node(NIL, NIL, [NIL]) for _ in range(n)]
    depths = [0] * n
    for i in inputs:
        input = list(map(int, i.split()))
        c = int(input[0])
        k = int(input[1])
        if len(input) > 2:
            rights = input[2:]
            if k != len(rights):
                raise ValueError("invalid input")
            cl[c].right = rights
            for j in rights:
                cl[j].parent = c
    for i in range(n):
        if cl[i].parent == NIL:
            root = i
    set_depth(cl, root, depths, 0)
    for c in range(n):
        type = "internal node"
        if cl[c].parent == NIL:
            type = "root"
        if cl[c].right == [NIL]:
            cl[c].right = []
            if cl[c].parent != NIL:
                type = "leaf"
        print(
            f"node {c}: parent = {cl[c].parent}, depth = {depths[c]}, {type}, {cl[c].right}"
        )


if __name__ == "__main__":
    main()
