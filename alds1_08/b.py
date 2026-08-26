# Binary Search Tree II


from sys import stdin


class Node:
    def __init__(self, key):
        self.key = key if validate_key(key) else None
        self.parent = None
        self.left = None
        self.right = None


def validate_key(key):
    return -2_000_000_000 <= key <= 2_000_000_000


def insert(root, node):
    x = root
    y = None
    while x is not None:
        y = x
        if node.key < x.key:
            x = x.left
        else:
            x = x.right
    node.parent = y
    if y is None:
        root = node
    elif node.key < y.key:
        y.left = node
    else:
        y.right = node
    return root


def find(root, key):
    while root is not None and key != root.key:
        if key < root.key:
            root = root.left
        else:
            root = root.right
    return root


def pre_parse(node):
    if node is None:
        return
    print(f" {node.key}", end="")
    pre_parse(node.left)
    pre_parse(node.right)


def in_parse(node):
    if node is None:
        return
    in_parse(node.left)
    print(f" {node.key}", end="")
    in_parse(node.right)


def main():
    n = int(stdin.readline())
    inputs = stdin.readlines()
    root = None
    if n != len(inputs):
        raise ValueError("invalid input")
    for line in inputs:
        input = line.split()
        if input[0] == "insert":
            node = Node(int(input[1]))
            root = insert(root, node)
        elif input[0] == "print":
            in_parse(root)
            print()
            pre_parse(root)
            print()
        elif input[0] == "find":
            print("yes" if find(root, int(input[1])) is not None else "no")


if __name__ == "__main__":
    main()
