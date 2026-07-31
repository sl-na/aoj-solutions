# Insertion Sort


def trace(A: list[int], N: int):
    for i in range(N):
        if i > 0:
            print(" ", end="")
        print(A[i], end="")
    print()


def insertion_sort(A: list[int], N: int):
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        trace(A, N)


def main():
    A: list[int] = [] * 100
    N = int(input())
    A: list[int] = list(map(int, input().split()))
    trace(A, N)
    insertion_sort(A, N)


if __name__ == "__main__":
    main()
