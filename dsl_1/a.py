# Disjoint Set: Union Find Tree


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


def main():
    it = map(int, sys.stdin.read().split())
    n, q = next(it), next(it)
    uf = UnionFind(n)
    answer = []
    for _ in range(q):
        com, x, y = next(it), next(it), next(it)
        if com == 0:
            uf.union(x, y)
        elif com == 1:
            if uf.is_same(x, y):
                answer.append("1")
            else:
                answer.append("0")
    print("\n".join(answer))


if __name__ == "__main__":
    main()
