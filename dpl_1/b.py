# 0-1 Knapsack Problem

import sys


def knapsack(n, weight, items):
    costs = [[0] * (weight + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, weight + 1):
            if items[i][1] <= w:
                if items[i][0] + costs[i - 1][w - items[i][1]] > costs[i - 1][w]:
                    costs[i][w] = items[i][0] + costs[i - 1][w - items[i][1]]
                else:
                    costs[i][w] = costs[i - 1][w]
            else:
                costs[i][w] = costs[i - 1][w]
    return costs[n][weight]


def main():
    it = map(int, sys.stdin.read().split())
    n, w = next(it), next(it)
    items = [(0, 0)]
    for item_v, item_w in zip(it, it):
        items.append((item_v, item_w))
    print(knapsack(n, w, items))


if __name__ == "__main__":
    main()
