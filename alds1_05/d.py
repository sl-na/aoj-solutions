# The Number of Inversions


from math import inf
from sys import stdin


def validate_list(al):
    return [i for i in al if 0 <= i <= 10**9]


def merge(al, left, mid, right):
    left_l = al[left:mid] + [inf]
    right_l = al[mid:right] + [inf]
    cnt = i = j = 0
    for k in range(left, right):
        if left_l[i] <= right_l[j]:
            al[k] = left_l[i]
            i += 1
        else:
            al[k] = right_l[j]
            j += 1
            cnt += len(left_l) - 1 - i
    return cnt


def merge_sort(al, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        v1 = merge_sort(al, left, mid)
        v2 = merge_sort(al, mid, right)
        v3 = merge(al, left, mid, right)
        return v1 + v2 + v3
    else:
        return 0


def main():
    n = int(stdin.readline())
    al = list(map(int, stdin.readline().split()))
    if n != len(al):
        raise ValueError(
            "the length of the second input must be the same as the first input value"
        )
    al = validate_list(al)
    print(merge_sort(al, 0, n))


if __name__ == "__main__":
    main()
