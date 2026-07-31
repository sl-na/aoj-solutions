# Depth First Search


from sys import stdin


def dfs(graph):
    n = len(graph)
    visited = [False] * n
    dl = [None] * n
    fl = [None] * n
    time = 0

    for i in range(n):
        if visited[i]:
            continue
        stack = [(i, False)]
        while stack:
            v, finished = stack.pop()
            if not finished:
                if visited[v]:
                    continue
                visited[v] = True
                time += 1
                dl[v] = time
                stack.append((v, True))
                for neighbor in reversed(graph[v]):
                    if not visited[neighbor]:
                        stack.append((neighbor, False))
            else:
                time += 1
                fl[v] = time

    return dl, fl


def main():
    row = int(stdin.readline())
    inputs = [list(map(int, line.split())) for line in stdin]
    if row != len(inputs):
        raise ValueError("invalid input")
    graph = [[i - 1 for i in j[2:]] for j in inputs]
    dl, fl = dfs(graph)
    answer = [f"{i + 1} {dl[i]} {fl[i]}" for i in range(row)]
    print("\n".join(answer))


if __name__ == "__main__":
    main()
