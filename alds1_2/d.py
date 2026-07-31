# Shell Sort


import sys

cnt = 0
G: list[int] = []


def insertion_sort(A, n, g):
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            global cnt
            cnt += 1
        A[j + g] = v


def shell_sort(A, n):
    global G
    h = 1
    while h < n:
        G.append(h)
        h = 3 * h + 1
    for i in range(len(G) - 1, -1, -1):
        insertion_sort(A, n, G[i])


def main():
    n = int(input())
    A = [0] * 1000000
    for i in range(n):
        A[i] = int(sys.stdin.readline())
    shell_sort(A, n)
    print(len(G))
    for i in range(len(G) - 1, -1, -1):
        print(G[i], end="")
        if i != 0:
            print(end=" ")
    print()
    global cnt
    print(cnt)
    for i in range(n):
        print(A[i])


if __name__ == "__main__":
    main()
