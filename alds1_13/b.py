# 8 Puzzle

import sys
from collections import deque
from dataclasses import dataclass

N = 3
N2 = N * N


@dataclass
class Puzzle:
    state: list[int]
    space: int
    path: list[str]


def is_target(puzzle):
    for i in range(N2):
        if puzzle.state[i] != i + 1:
            return False
    return True


def bfs(puzzle):
    moves = {"Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1)}
    queue = deque([puzzle])
    visited = {tuple(puzzle.state)}
    while queue:
        curr_p = queue.popleft()
        if is_target(curr_p):
            return curr_p.path
        row = curr_p.space // N
        col = curr_p.space % N
        for move, (diff_r, diff_c) in moves.items():
            next_r = row + diff_r
            next_c = col + diff_c
            if not (0 <= next_r < N and 0 <= next_c < N):
                continue
            new_state = list(curr_p.state)
            new_space = next_r * N + next_c
            new_state[curr_p.space], new_state[new_space] = (
                new_state[new_space],
                new_state[curr_p.space],
            )
            next_p = Puzzle(new_state, new_space, curr_p.path + [move])
            if tuple(next_p.state) not in visited:
                visited.add(tuple(next_p.state))
                queue.append(next_p)


def main():
    it = map(int, sys.stdin.read().split())
    board = []
    space_idx = -1
    for i in range(N2):
        val = next(it)
        if val == 0:
            val = N2
            space_idx = i
        board.append(val)
    init_state = Puzzle(board, space_idx, [])
    answer = bfs(init_state)
    print(len(answer))


if __name__ == "__main__":
    main()
