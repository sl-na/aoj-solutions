# Quick Sort


from dataclasses import dataclass
from math import inf
from sys import stdin


@dataclass
class Card:
    suit: str
    value: int


def validate_list(card_list):
    return [i for i in card_list if 1 <= i.value <= 10**9]


def merge(bl, left, mid, right):
    left_l = bl[left:mid] + [inf]
    right_l = bl[mid:right] + [inf]
    i = j = 0
    k = left
    for k in range(left, right):
        if right_l[j] == inf and left_l[i] != inf:
            bl[k] = left_l[i]
            i += 1
        elif left_l[i] == inf and right_l[j] != inf:
            bl[k] = right_l[j]
            j += 1
        else:
            if left_l[i].value <= right_l[j].value:
                bl[k] = left_l[i]
                i += 1
            else:
                bl[k] = right_l[j]
                j += 1


def merge_sort(bl, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(bl, left, mid)
        merge_sort(bl, mid, right)
        merge(bl, left, mid, right)


def partition(al, p, right):
    x = al[right].value
    i = p - 1
    for j in range(p, right):
        if al[j].value <= x:
            i += 1
            al[i], al[j] = al[j], al[i]
    al[i + 1], al[right] = al[right], al[i + 1]
    return i + 1


def quick_sort(al, p, right):
    if p < right:
        q = partition(al, p, right)
        quick_sort(al, p, q - 1)
        quick_sort(al, q + 1, right)


def main():
    n = int(stdin.readline())
    inputs = stdin.readlines()
    al = bl = [Card("", 0)] * n
    is_stable = True
    for i in range(n):
        suit = inputs[i][0]
        value = int(inputs[i][1:])
        al[i] = bl[i] = Card(suit, value)
    al = validate_list(al)
    bl = validate_list(bl)
    quick_sort(al, 0, n - 1)
    merge_sort(bl, 0, n)
    for i in range(n):
        if al[i].suit != bl[i].suit:
            is_stable = False
    print("Stable" if is_stable else "Not stable")
    for i in range(n):
        print(al[i].suit, al[i].value)


if __name__ == "__main__":
    main()
