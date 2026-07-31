# Counting Sort


from math import inf
from sys import stdin


def validate_list(al):
    return [i for i in al if 0 <= i <= 10000]


def counting_sort(al, bl, k):
    cl = [0] * (k + 1)
    for i in range(len(al)):
        cl[al[i]] += 1
    for i in range(1, k + 1):
        cl[i] = cl[i] + cl[i - 1]
    for i in range(len(al) - 1, -1, -1):
        cl[al[i]] -= 1
        bl[cl[al[i]]] = al[i]


def main():
    n = int(stdin.readline())
    al = list(map(int, stdin.readline().split()))
    if len(al) != n:
        raise ValueError(
            "the length of the second input must be the same as the first input value"
        )
    al = validate_list(al)
    bl = [inf] * len(al)
    k = max(al)
    counting_sort(al, bl, k)
    for index, value in enumerate(bl):
        if index == len(bl) - 1:
            print(value)
        else:
            print(value, end=" ")


if __name__ == "__main__":
    main()
