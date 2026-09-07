# Largest Square

import sys


def largest_square(h, w, grid):
    dp = [[0] * (w + 1) for _ in range(h + 1)]
    max_side = 0
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if grid[i - 1][j - 1] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                max_side = max(max_side, dp[i][j])
    return max_side**2


def main():
    it = map(int, sys.stdin.read().split())
    h, w = next(it), next(it)
    grid = [[next(it) for _ in range(w)] for _ in range(h)]
    print(largest_square(h, w, grid))


if __name__ == "__main__":
    main()
