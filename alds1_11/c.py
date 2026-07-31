# Breadth First Search


from collections import deque
from sys import stdin


def bfs(graph, start):
    n = len(graph)
    dl = [-1] * n
    queue = deque()
    queue.append(start)
    dl[start] = 0
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if dl[neighbor] == -1:
                dl[neighbor] = dl[v] + 1
                queue.append(neighbor)
    return dl


def main():
    row = int(stdin.readline())
    inputs = list(map(list[int], [map(int, line.split()) for line in stdin]))
    if row != len(inputs):
        raise ValueError("invalid input")
    graph = list(map(list[int], [[i - 1 for i in j[2:]] for j in inputs]))
    dl = bfs(graph, 0)
    answer = list(map(str, [f"{i + 1} {dl[i]}" for i in range(row)]))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
