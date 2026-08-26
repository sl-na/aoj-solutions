# Priority Queue


import sys
from math import inf


def validate_key(key):
    return 0 <= key <= 2_000_000_000


def max_heapify(heap_size, al, i):
    left = 2 * i
    right = 2 * i + 1
    if left <= heap_size and al[left] > al[i]:
        largest = left
    else:
        largest = i
    if right <= heap_size and al[right] > al[largest]:
        largest = right
    if largest != i:
        al[i], al[largest] = al[largest], al[i]
        max_heapify(heap_size, al, largest)


def insert(heap_size, queues, key):
    if not validate_key(key):
        raise ValueError("invalid key")
    queues[heap_size] = -inf
    increase_key(heap_size, queues, key)


def increase_key(i, queues, key):
    if key < queues[i]:
        return
    queues[i] = key
    while i > 1 and queues[i // 2] < queues[i]:
        queues[i], queues[i // 2] = queues[i // 2], queues[i]
        i = i // 2


def extract_max(heap_size, queues):
    maxv = queues[1]
    queues[1] = queues[heap_size]
    max_heapify(heap_size, queues, 1)
    return maxv


def main():
    queues = [-inf] * 2_000_000
    heap_size = 0
    inputs = sys.stdin.readlines()
    for line in inputs:
        input = line.split()
        if input[0] == "end":
            sys.exit()
        elif input[0] == "insert":
            heap_size += 1
            insert(heap_size, queues, int(input[1]))
        elif input[0] == "extract":
            print(extract_max(heap_size, queues))
            heap_size -= 1
        else:
            raise AssertionError("invalid command")


if __name__ == "__main__":
    main()
