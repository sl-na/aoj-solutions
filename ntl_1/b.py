# Power

import sys


def main():
    m, n = map(int, sys.stdin.read().split())
    print(pow(m, n, 1000000007))


if __name__ == "__main__":
    main()
