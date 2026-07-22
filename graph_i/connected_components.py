from sys import stdin


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents: list[int | None] = [None for _ in range(n)]
        self.sizes = [1] * n

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
