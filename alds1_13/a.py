# 8 Queens Problem

import sys

N = 8
FREE = -1
NOT_FREE = 1


def print_board(row):
    for i in range(N):
        for j in range(N):
            print("Q" if row[i] == j else ".", end="")
        print()


def place_queens(i, grid, row, col, dpos, dneg):
    if i == N:
        print_board(row)
        return
    if grid[i][row[i]]:
        place_queens(i + 1, grid, row, col, dpos, dneg)
        return
    for j in range(N):
        if (
            col[j] == NOT_FREE
            or dpos[i + j] == NOT_FREE
            or dneg[i - j + N - 1] == NOT_FREE
        ):
            continue
        row[i] = j
        col[j] = dpos[i + j] = dneg[i - j + N - 1] = NOT_FREE
        place_queens(i + 1, grid, row, col, dpos, dneg)
        row[i] = col[j] = dpos[i + j] = dneg[i - j + N - 1] = FREE


def main():
    it = map(int, sys.stdin.read().split())
    _ = next(it)
    grid = [[False] * N for _ in range(N)]
    row = [FREE] * N
    col = [FREE] * N
    dpos = [FREE] * (2 * N - 1)
    dneg = [FREE] * (2 * N - 1)
    for r, c in zip(it, it):
        grid[r][c] = True
        row[r] = c
        col[c] = dpos[r + c] = dneg[r - c + N - 1] = NOT_FREE
    place_queens(0, grid, row, col, dpos, dneg)


if __name__ == "__main__":
    main()
