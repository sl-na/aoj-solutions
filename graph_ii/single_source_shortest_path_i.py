import sys
from heapq import heappop, heappush
from math import inf


def dijkstra(adj_list, s):
    n = len(adj_list)
    dist_list = [inf for _ in range(n)]
    dist_list[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heappop(pq)
        if d > dist_list[u]:
            continue
        for v, c in adj_list[u]:
            new_dist = d + c
            if new_dist < dist_list[v]:
                dist_list[v] = new_dist
                heappush(pq, (new_dist, v))
    return dist_list


def main():
    it = map(int, sys.stdin.read().split())
    n = next(it)
    adj_list = [[] for _ in range(n)]
    for _ in range(n):
        u = next(it)
        k = next(it)
        for _ in range(k):
            v = next(it)
            c = next(it)
            adj_list[u].append((v, c))
    dist_list = dijkstra(adj_list, 0)
    answer = "\n".join(f"{i} {dist}" for i, dist in enumerate(dist_list))
    print(answer)


if __name__ == "__main__":
    main()
