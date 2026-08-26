# Allocation

import sys

MAX = 100000
T = [] * MAX
n = 0
k = 0


def check(p):
    i = 0
    for j in range(k):
        s = 0
        while s + T[i] <= p:
            s += T[i]
            i += 1
            if i == n:
                return n
    return i


def solve():
    left = 0
    right = 100000 * 10000
    while (right - left) > 1:
        mid = (left + right) // 2
        v = check(mid)
        if v >= n:
            right = mid
        else:
            left = mid
    return right


def main():
    global n
    global k
    n, k = list(map(int, sys.stdin.readline().split()))
    line = list(map(int, sys.stdin.read().splitlines()))
    for i in line:
        T.append(i)
    answer = solve()
    print(answer)


if __name__ == "__main__":
    main()
