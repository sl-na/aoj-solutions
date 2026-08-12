# Diameter of a Tree

import sys
from collections import deque


def bfs(s, adj_list):
    n = len(adj_list)
    dists = [-1] * n
    dists[s] = 0
    queue = deque()
    queue.append(s)
    farthest_node = s
    max_dist = 0
    while queue:
        u = queue.popleft()
        for neighbor, weight in adj_list[u]:
            if dists[neighbor] == -1:
                dists[neighbor] = dists[u] + weight
                queue.append(neighbor)
                if dists[neighbor] > max_dist:
                    max_dist = dists[neighbor]
                    farthest_node = neighbor
    return farthest_node, max_dist


def main():
    it = map(int, sys.stdin.read().split())
    n = next(it)
    adj_list = [[] for _ in range(n)]
    for s, t, w in zip(it, it, it):
        adj_list[s].append((t, w))
        adj_list[t].append((s, w))
    u, _ = bfs(0, adj_list)
    _, max_dist = bfs(u, adj_list)
    print(max_dist)


if __name__ == "__main__":
    main()
