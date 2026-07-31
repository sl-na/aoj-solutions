# Merge Sort


from math import inf
from sys import stdin

cnt = 0


def validate_list(nl):
    return [i for i in nl if 0 <= i <= 10**9]


def merge(nl, left, mid, right):
    left_l = nl[left:mid] + [inf]
    right_l = nl[mid:right] + [inf]
    i = j = 0
    k = left
    global cnt
    for k in range(left, right):
        if left_l[i] <= right_l[j]:
            nl[k] = left_l[i]
            i += 1
        else:
            nl[k] = right_l[j]
            j += 1
        cnt += 1


def merge_sort(nl, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(nl, left, mid)
        merge_sort(nl, mid, right)
        merge(nl, left, mid, right)


def main():
    n = int(stdin.readline())
    nl = list(map(int, stdin.readline().split()))
    nl = validate_list(nl)
    if n != len(nl):
        raise ValueError(
            "the length of the second input must be the same as the first input value. or there is an out of range value in the input."
        )
    merge_sort(nl, 0, n)
    for index, value in enumerate(nl):
        if index != len(nl) - 1:
            print(value, end=" ")
        else:
            print(value)
    print(cnt)


if __name__ == "__main__":
    main()
