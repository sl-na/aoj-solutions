# Coin Changing Problem

import sys
from functools import lru_cache
from math import inf


@lru_cache(maxsize=10**6)
def min_coins(n, coins):
    dp = [inf] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[n]


def main():
    it = map(int, sys.stdin.read().split())
    n, _ = next(it), next(it)
    coins = frozenset(i for i in it)
    print(min_coins(n, coins))


if __name__ == "__main__":
    main()
