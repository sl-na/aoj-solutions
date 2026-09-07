# Longest Increasing Subsequence

import sys
from bisect import bisect_left


def lis(a):
    n = len(a)
    l = [0] * (n + 1)
    length = 1
    l[0] = a[0]
    for i in range(1, n):
        if a[i] > l[length - 1]:
            l[length] = a[i]
            length += 1
        else:
            idx = bisect_left(l, a[i], 0, length)
            l[idx] = a[i]
    return length


def main():
    it = map(int, sys.stdin.read().split())
    _ = next(it)
    a = list(it)
    print(lis(a))


if __name__ == "__main__":
    main()
