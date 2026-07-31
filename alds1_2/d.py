# Shell Sort


import sys

cnt = 0
G: list[int] = []


def insertion_sort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            cnt += 1
        A[j + g] = v


def shell_sort(A, n):
    h = 1
    while h <= n:
        G.append(h)
        h = 3 * h + 1
    for i in range(len(G) - 1, -1, -1):
        insertion_sort(A, n, G[i])


def main():
    n = int(input())
    A = [0] * n
    it = map(int, sys.stdin.read().split())
    for i in range(n):
        A[i] = next(it)
    shell_sort(A, n)
    print(len(G))
    g_answer = ""
    for i in range(len(G) - 1, -1, -1):
        g_answer += str(G[i])
        if i != 0:
            g_answer += " "
    print(g_answer, end="")
    print()
    print(cnt)
    print("\n".join(map(str, A)))


if __name__ == "__main__":
    main()
