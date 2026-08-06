# Shell Sort


import sys


def insertion_sort(A, n, g, cnt):
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            cnt += 1
        A[j + g] = v
    return cnt


def shell_sort(A, n, G):
    cnt = 0
    h = 1
    while h <= n:
        G.append(h)
        h = 3 * h + 1
    for i in range(len(G) - 1, -1, -1):
        cnt = insertion_sort(A, n, G[i], cnt)
    return cnt


def main():
    it = map(int, sys.stdin.read().split())
    n = next(it)
    A = [next(it) for _ in range(n)]
    G = []
    cnt = shell_sort(A, n, G)
    answer = []
    answer.append(str(len(G)))
    g_answer = " ".join(str(G[i]) for i in range(len(G) - 1, -1, -1))
    answer.append(g_answer)
    answer.append(str(cnt))
    answer.extend(map(str, A))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
