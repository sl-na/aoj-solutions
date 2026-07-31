# Selection Sort


def selection_sort(A: list[int], N: int):
    sw = 0
    minj = None
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        t = A[i]
        A[i] = A[minj]
        A[minj] = t
        if i != minj:
            sw += 1
    return sw


def main():
    A: list[int] = [] * 100
    N = int(input())
    A = list(map(int, input().split()))
    sw = selection_sort(A, N)
    for i in range(N):
        if i > 0:
            print(" ", end="")
        print(A[i], end="")
    print()
    print(sw)


if __name__ == "__main__":
    main()
