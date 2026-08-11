# Topological Sort


import sys
from collections import deque


def topological_sort(adj_list, in_degree):
    in_degree = in_degree.copy()
    v = len(adj_list)
    queue = deque([u for u in range(v) if in_degree[u] == 0])
    output = []
    while queue:
        u = queue.popleft()
        output.append(u)
        for neighbor in adj_list[u]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return output


def main():
    it = map(int, sys.stdin.read().split())
    v, e = next(it), next(it)
    adj_list = [[] for _ in range(v)]
    in_degree = [0 for _ in range(v)]
    for _ in range(e):
        s, t = next(it), next(it)
        adj_list[s].append(t)
        in_degree[t] += 1
    answer = topological_sort(adj_list, in_degree)
    print("\n".join(map(str, answer)))


if __name__ == "__main__":
    main()
