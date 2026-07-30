import sys


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = list(range(n))
        self.sizes = [1 for _ in range(n)]

    def find(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.sizes[x] < self.sizes[y]:
            x, y = y, x
        self.parents[y] = x
        self.sizes[x] += self.sizes[y]


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
