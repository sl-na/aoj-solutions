# Matrix Chain Multiplication

import math
from sys import stdin


def main():
    n = int(stdin.readline())
    inputs = [[int(i) for i in line.split()] for line in stdin.readlines()]
    pl = [i for i, _ in inputs]
    pl.append(inputs[-1][1])
    dp = [[math.inf] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][i] = 0
    for l in range(n + 1):
        for i in range(n - l + 1):
            j = i + l
            for k in range(i, j):
                dp[i][j] = min(
                    dp[i][j], dp[i][k] + dp[k + 1][j] + pl[i - 1] * pl[k] * pl[j]
                )
    print(dp[0][n - 1])


if __name__ == "__main__":
    main()
