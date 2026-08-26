# Dictionary


import sys

M = 1046527


def get_char(char: str) -> int:
    if char == "A":
        return 1
    elif char == "C":
        return 2
    elif char == "G":
        return 3
    elif char == "T":
        return 4
    else:
        return 0


def get_key(char: str):
    key = 0
    for ch in char:
        key = key * 5 + get_char(ch)
    return key


def hash1(key):
    return key % M


def hash2(key):
    return 1 + (key % (M - 1))


def insert(list, char: str) -> bool:
    key = get_key(char)
    i = 0
    while True:
        h = (hash1(key) + i * hash2(key)) % M
        if list[h] is None:
            list[h] = char
            return True
        elif list[h] == char:
            return False
        i += 1


def find(list, char: str) -> bool:
    key = get_key(char)
    i = 0
    while True:
        h = (hash1(key) + i * hash2(key)) % M
        if list[h] is None:
            return False
        elif list[h] == char:
            return True
        i += 1


def main():
    n = int(sys.stdin.readline())
    if not n <= 1000000:
        raise ValueError("the first input value must be less than or equal to 1000000")
    nodes = sys.stdin.read().splitlines()
    list = [None] * M
    if len(nodes) != n:
        raise ValueError("input data length is not equal to the first input data")
    for line in nodes:
        func, key = line.split()
        if func == "insert":
            insert(list, key)
        elif func == "find":
            if find(list, key):
                print("yes")
            else:
                print("no")


if __name__ == "__main__":
    main()
