# All Pairs Shortest Path


import sys
from math import inf


def warshall_floyd(adj_matrix):
    n = len(adj_matrix)
    for k in range(n):
        for i in range(n):
            if adj_matrix[i][k] == inf:
                continue
            for j in range(n):
                if adj_matrix[k][j] == inf:
                    continue
                adj_matrix[i][j] = min(
                    adj_matrix[i][j], adj_matrix[i][k] + adj_matrix[k][j]
                )


def has_negative_cycle(adj_matrix):
    n = len(adj_matrix)
    return any(adj_matrix[i][i] < 0 for i in range(n))


def main():
    it = map(int, sys.stdin.read().split())
    v, e = next(it), next(it)
    adj_matrix = [[inf if i != j else 0 for j in range(v)] for i in range(v)]
    for _ in range(e):
        s, t, d = next(it), next(it), next(it)
        adj_matrix[s][t] = d
    warshall_floyd(adj_matrix)
    if has_negative_cycle(adj_matrix):
        print("NEGATIVE CYCLE")
        return
    answer = [[] for _ in range(v)]
    for i in range(v):
        for j in adj_matrix[i]:
            answer[i].append("INF" if j == inf else str(j))
    print("\n".join(" ".join(i) for i in answer))


if __name__ == "__main__":
    main()
