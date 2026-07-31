# Tree Walk


from sys import stdin

NIL = -1


class Node:
    def __init__(self):
        self.parent = NIL
        self.left = NIL
        self.right = NIL


def pre_parse(bt, index):
    if index == NIL:
        return
    print(f" {index}", end="")
    pre_parse(bt, bt[index].left)
    pre_parse(bt, bt[index].right)


def in_parse(bt, index):
    if index == NIL:
        return
    in_parse(bt, bt[index].left)
    print(f" {index}", end="")
    in_parse(bt, bt[index].right)


def post_parse(bt, index):
    if index == NIL:
        return
    post_parse(bt, bt[index].left)
    post_parse(bt, bt[index].right)
    print(f" {index}", end="")


def main():
    n = int(stdin.readline())
    inputs = stdin.readlines()
    bt = [Node() for _ in range(n)]
    for index, value in enumerate(inputs):
        input = list(map(int, value.split()))
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
    print("Preorder")
    pre_parse(bt, root)
    print()
    print("Inorder")
    in_parse(bt, root)
    print()
    print("Postorder")
    post_parse(bt, root)
    print()


if __name__ == "__main__":
    main()
