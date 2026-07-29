import sys


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [None for _ in range(n)]
        self.sizes = [1 for _ in range(n)]

    def find(self, x):
        if self.parents[x] is None:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, s, t):
        s = self.find(s)
        t = self.find(t)
        if s == t:
            return
        if self.sizes[s] < self.sizes[t]:
            s, t = t, s
        self.parents[t] = s
        self.sizes[s] += self.sizes[t]

    def is_same(self, s, t):
        return self.find(s) == self.find(t)


def kruskal(edges):
    n = len(edges)
    edges.sort()
    uf = UnionFind(n)
    total_weight = 0
    for weight, (s, t) in edges:
        if uf.is_same(s, t):
            continue
        else:
            total_weight += weight
            uf.union(s, t)
    return total_weight


def main():
    n = int(sys.stdin.readline())
    adj_matrix = list(map(int, sys.stdin.read().split()))
    edges = [
        (adj_matrix[i * n + j], (i, j))
        for i in range(n)
        for j in range(i + 1, n)
        if adj_matrix[i * n + j] >= 0
    ]
    print(kruskal(edges))


if __name__ == "__main__":
    main()
