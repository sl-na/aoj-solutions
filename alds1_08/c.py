# Binary Search Tree III


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
    current = root
    while current is not None and key != current.key:
        if key < current.key:
            current = current.left
        else:
            current = current.right
    return current


def delete(root, key):
    if key.left is None or key.right is None:
        target = key
    else:
        target = get_successor(key)
    if target.left is not None:
        child = target.left
    else:
        child = target.right
    if child is not None:
        child.parent = target.parent
    if target.parent is None:
        root = child
        return root
    else:
        if target == target.parent.left:
            target.parent.left = child
        else:
            target.parent.right = child
    if target != key:
        key.key = target.key
    return root


def get_successor(key):
    if key.right is not None:
        return get_minimum(key.right)
    target = key.parent
    while target is not None and key == target.right:
        key = target
        target = target.parent
    return target


def get_minimum(key):
    while key.left is not None:
        key = key.left
    return key


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
        elif input[0] == "delete":
            node = find(root, int(input[1]))
            root = delete(root, node)


if __name__ == "__main__":
    main()
