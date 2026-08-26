# Complete Binary Tree


from sys import stdin


def validate_key(key):
    return -2_000_000_000 <= key <= 2_000_000_000


def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def main():
    n = int(stdin.readline())
    inputs = [None] + list(map(int, stdin.readline().split()))
    for i in range(1, n + 1):
        if not validate_key(inputs[i]):
            raise ValueError("invalid key")
        print(f"node {i}: key = {inputs[i]}, ", end="")
        if parent(i) >= 1:
            print(f"parent key = {inputs[parent(i)]}, ", end="")
        if left(i) <= n:
            print(f"left key = {inputs[left(i)]}, ", end="")
        if right(i) <= n:
            print(f"right key = {inputs[right(i)]}, ", end="")
        print()


if __name__ == "__main__":
    main()
