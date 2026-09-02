# Coin Changing Problem

import sys
from math import inf


def min_coins(n, coins):
    dp = [inf] * (n + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, n + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[n]


def main():
    it = map(int, sys.stdin.read().split())
    n, _ = next(it), next(it)
    coins = list(it)
    print(min_coins(n, coins))


if __name__ == "__main__":
    main()
