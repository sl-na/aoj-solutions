# Articulation Points


import sys

sys.setrecursionlimit(10**6)


class LowLink:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.order = [-1] * n
        self.low = [0] * n
        self.articulation_points = set()
        self._timer = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def _dfs(self, u, p):
        self.low[u] = self.order[u] = self._timer
        self._timer += 1
        children = 0
        for v in self.graph[u]:
            if v == p:
                continue
            if self.order[v] != -1:
                self.low[u] = min(self.low[u], self.order[v])
            else:
                children += 1
                self._dfs(v, u)
                self.low[u] = min(self.low[u], self.low[v])
                if p != -1 and self.low[v] >= self.order[u]:
                    self.articulation_points.add(u)
        if p == -1 and children > 1:
            self.articulation_points.add(u)

    def get_articulation_points(self):
        self._timer = 0
        for i in range(self.n):
            if self.order[i] == -1:
                self._dfs(i, -1)
        return sorted(self.articulation_points)


def main():
    it = map(int, sys.stdin.read().split())
    v, _ = next(it), next(it)
    low_link = LowLink(v)
    for s, t in zip(it, it):
        low_link.add_edge(s, t)
    articulation_points = low_link.get_articulation_points()
    if articulation_points:
        print("\n".join(map(str, articulation_points)))


if __name__ == "__main__":
    main()
