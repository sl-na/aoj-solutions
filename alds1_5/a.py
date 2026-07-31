# Exhaustive Search


from sys import stdin


def solve(i, mt, n, at):
    if mt == 0:
        return True
    if i >= n:
        return False
    return solve(i + 1, mt, n, at) or solve(i + 1, mt - at[i], n, at)


def main():
    n = int(stdin.readline())
    at = tuple(map(int, stdin.readline().split()))
    q = int(stdin.readline())
    mt = tuple(map(int, stdin.readline().split()))
    for i in range(q):
        if solve(0, mt[i], n, at):
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()
