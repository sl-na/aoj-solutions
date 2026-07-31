# Stable Sort


from dataclasses import dataclass


@dataclass
class Card:
    suit: str
    value: int


def bubble(A, N: int):
    for i in range(N):
        for j in range(N - 1, i, -1):
            if A[j].value < A[j - 1].value:
                t: Card = A[j]
                A[j] = A[j - 1]
                A[j - 1] = t


def selection(A, N: int):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j].value < A[minj].value:
                minj = j
        t = A[i]
        A[i] = A[minj]
        A[minj] = t


def print_card(A, N: int):
    for i in range(N):
        if i > 0:
            print(" ", end="")
        print(f"{A[i].suit}{A[i].value}", end="")
    print()


def is_stable(C1, C2, N: int):
    for i in range(N):
        if C1[i].suit != C2[i].suit:
            return False
    return True


def main():
    C1 = [None] * 100
    C2 = [None] * 100
    N = int(input())
    inputs = input().split()
    for i in range(N):
        suit = inputs[i][0]
        value = int(inputs[i][1:])
        C1[i] = Card(suit, value)
    for i in range(N):
        C2[i] = C1[i]
    bubble(C1, N)
    selection(C2, N)
    print_card(C1, N)
    print("Stable")
    print_card(C2, N)
    if is_stable(C1, C2, N):
        print("Stable")
    else:
        print("Not stable")


if __name__ == "__main__":
    main()
