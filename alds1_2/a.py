# Bubble Sort


def bubble_sort(A: list[int], N: int):
    sw = 0
    flag = True
    while flag:
        flag = False
        for j in range(N - 1, 0, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                flag = True
                sw += 1
    return sw


def main():
    A: list[int] = [] * 100
    N = int(input())
    A = list(map(int, input().split()))
    sw = bubble_sort(A, N)

    for i in range(N):
        if i:
            print(" ", end="")
        print(A[i], end="")
    print()
    print(sw)


if __name__ == "__main__":
    main()
