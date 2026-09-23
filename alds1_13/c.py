# 15 Puzzle

import sys

N = 4
N2 = N * N
MDT = [
    [abs(i // N - j // N) + abs(i % N - j % N) for j in range(N2)] for i in range(N2)
]
DY = [-1, 1, 0, 0]
DX = [0, 0, -1, 1]


def calc_manhattan_distance(state):
    sum_md = 0
    for i, val in enumerate(state):
        if val != N2:
            sum_md += MDT[i][val - 1]
    return sum_md


def dfs(state, space, md, depth, limit, prev):
    estimated = depth + md
    if limit < estimated:
        return False, estimated
    if md == 0:
        return True, depth
    min_next_limit = float("inf")
    row = space // N
    col = space % N
    for i in range(4):
        if prev != -1 and (i ^ 1) == prev:
            continue
        next_r = row + DY[i]
        next_c = col + DX[i]
        if not (0 <= next_r < N and 0 <= next_c < N):
            continue
        next_space = next_r * N + next_c
        next_val = state[next_space]
        next_md = md - MDT[next_space][next_val - 1] + MDT[space][next_val - 1]
        state[space], state[next_space] = state[next_space], state[space]

        found, next_limit = dfs(state, next_space, next_md, depth + 1, limit, i)
        state[space], state[next_space] = state[next_space], state[space]
        if found:
            return True, next_limit
        min_next_limit = min(min_next_limit, next_limit)
    return False, min_next_limit


def iterative_deepening(state, space):
    init_md = calc_manhattan_distance(state)
    limit = init_md
    while True:
        found, next_limit = dfs(state, space, init_md, 0, limit, -1)
        if found:
            return next_limit
        limit = next_limit


def main():
    it = map(int, sys.stdin.read().split())
    state = []
    space = -1
    for i, val in enumerate(it):
        if val == 0:
            val = N2
            space = i
        state.append(val)
    answer = iterative_deepening(state, space)
    print(answer)


if __name__ == "__main__":
    main()
