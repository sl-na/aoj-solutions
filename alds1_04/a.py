# Linear Search


import sys


def validate_list(int_list: list[int]) -> list[int]:
    validated_list: list[int] = []
    for i in int_list:
        if 0 <= i <= 10**9:
            validated_list.append(i)
        else:
            pass
    return validated_list


def linear_search(list: list[int], key: int) -> bool:
    for i in list:
        if i == key:
            return True
    return False


def main():
    n = int(sys.stdin.readline())
    if not n <= 10000:
        raise ValueError("the first input value must be less than or equal to 10000")
    s: list[int] = list(map(int, sys.stdin.readline().split()))
    if n != len(s):
        raise ValueError(
            "the length of the second input must be the same as the first input value"
        )
    s = validate_list(s)
    q = int(sys.stdin.readline())
    if not q <= 500:
        raise ValueError("the third input value must be less than or equal to 500")
    t: list[int] = list(map(int, sys.stdin.readline().split()))
    t = validate_list(t)
    if q != len(t):
        raise ValueError(
            "the length of the fourth input must be the same as the third input value"
        )
    c = 0
    for key in t:
        if linear_search(s, key):
            c += 1
    print(c)


if __name__ == "__main__":
    main()
