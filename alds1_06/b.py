# Partition


from sys import stdin


def validate_list(al):
    return [i for i in al if 0 <= i <= 100000]


def partition(al, p, right):
    x = al[right]
    i = p - 1
    for j in range(p, right):
        if al[j] <= x:
            i += 1
            al[i], al[j] = al[j], al[i]
    al[i + 1], al[right] = al[right], al[i + 1]
    return i + 1


def main():
    n = int(stdin.readline())
    al = list(map(int, stdin.readline().split()))
    al = validate_list(al)
    right = n - 1
    q = partition(al, 0, right)
    for i in range(n):
        if i >= 1:
            print(" ", end="")
        if i == q:
            print("[", end="")
        print(al[i], end="")
        if i == q:
            print("]", end="")
    print()


if __name__ == "__main__":
    main()
