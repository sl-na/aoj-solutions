# Binary Search


import sys


def validate_list(int_list: list[int]) -> list[int]:
    validated_list: list[int] = []
    for i in int_list:
        if 0 <= i <= 10**9:
            validated_list.append(i)
        else:
            pass
    return validated_list


def binary_search(int_list: list[int], key: int) -> bool:
    left = 0
    right = len(int_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if int_list[mid] == key:
            return True
        elif int_list[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return False


def main():
    n = int(sys.stdin.readline())
    if not n <= 100000:
        raise ValueError("the first input value must be less than or equal to 100000")
    s = list(map(int, sys.stdin.readline().split()))
    if n != len(s):
        raise ValueError(
            "the length of the second input must be the same as the first input value"
        )
    s = validate_list(s)
    q = int(sys.stdin.readline())
    t = list(map(int, sys.stdin.readline().split()))
    if q != len(t):
        raise ValueError(
            "the length of the fourth input must be the same as the third input value"
        )
    t = validate_list(t)
    c = 0
    for key in t:
        if binary_search(s, key):
            c += 1
    print(c)


if __name__ == "__main__":
    main()
