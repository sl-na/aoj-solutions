# Fibonacci Number


def main():
    n = int(input())
    fl: list[int | None] = [None] * (n + 1)
    fl[0] = fl[1] = 1
    for i in range(2, n + 1):
        left, right = fl[i - 1], fl[i - 2]
        assert left is not None and right is not None
        fl[i] = left + right
    print(fl[n])


if __name__ == "__main__":
    main()
