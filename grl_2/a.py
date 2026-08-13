# Minimum Spanning Tree

import sys


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.sizes[x] < self.sizes[y]:
            x, y = y, x
        self.parents[y] = x
        self.sizes[x] += self.sizes[y]
        return True


def kruskal(v, edges):
    edges.sort()
    uf = UnionFind(v)
    total_weight = 0
    edge_count = 0
    for w, s, t in edges:
        if uf.union(s, t):
            total_weight += w
            edge_count += 1
            if edge_count == v - 1:
                break
    return total_weight


def main():
    it = map(int, sys.stdin.read().split())
    v, _ = next(it), next(it)
    edges = [(w, s, t) for s, t, w in zip(it, it, it)]
    print(kruskal(v, edges))


if __name__ == "__main__":
    main()
