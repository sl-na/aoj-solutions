# Longest Common Subsequence


from sys import stdin


def lcs(xl, yl):
    m = len(xl)
    n = len(yl)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i, x in enumerate(xl, 1):
        for j, y in enumerate(yl, 1):
            if x == y:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def main():
    n = int(stdin.readline())
    for _ in range(n):
        xl = list(stdin.readline().strip())
        yl = list(stdin.readline().strip())
        print(lcs(xl, yl))


if __name__ == "__main__":
    main()
