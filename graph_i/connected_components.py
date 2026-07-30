from sys import stdin


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
    n, m = map(int, stdin.readline().split())
    uf = UnionFind(n)
    for _ in range(m):
        s, t = map(int, stdin.readline().split())
        uf.union(s, t)
    q = int(stdin.readline())
    answer: list[str] = []
    for _ in range(q):
        s, t = map(int, stdin.readline().split())
        answer.append("yes" if uf.is_same(s, t) else "no")
    print("\n".join(answer))


if __name__ == "__main__":
    main()
