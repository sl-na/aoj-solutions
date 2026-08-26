# Maximum Heap


from sys import stdin


def validate_key(key):
    return -2_000_000_000 <= key <= 2_000_000_000


def max_heapify(heap, al, i):
    left = 2 * i
    right = 2 * i + 1
    if left <= heap and al[left] > al[i]:
        largest = left
    else:
        largest = i
    if right <= heap and al[right] > al[largest]:
        largest = right
    if largest != i:
        al[i], al[largest] = al[largest], al[i]
        max_heapify(heap, al, largest)


def build_max_heap(heap, al):
    for i in range(heap // 2, 0, -1):
        max_heapify(heap, al, i)


def main():
    n = int(stdin.readline())
    inputs = [None] + list(map(int, stdin.readline().split()))
    for i in range(1, n + 1):
        if not validate_key(inputs[i]):
            raise ValueError("invalid key")
    build_max_heap(n, inputs)
    for i in range(1, n + 1):
        print(f" {inputs[i]}", end="")
    print()


if __name__ == "__main__":
    main()
