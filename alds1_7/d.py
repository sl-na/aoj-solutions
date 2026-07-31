# Reconstruction of a Tree


from sys import stdin


def reconstruct(pos, left, right, pre_order, in_order, post_order):
    if left >= right:
        return pos
    root = pre_order[pos]
    pos += 1
    mid = in_order.index(root)
    pos = reconstruct(pos, left, mid, pre_order, in_order, post_order)
    pos = reconstruct(pos, mid + 1, right, pre_order, in_order, post_order)
    post_order.append(root)
    return pos


def main():
    n = int(stdin.readline())
    pre_order = list(map(int, stdin.readline().split()))
    in_order = list(map(int, stdin.readline().split()))
    post_order = []
    reconstruct(0, 0, n, pre_order, in_order, post_order)
    print(" ".join(map(str, post_order)))


if __name__ == "__main__":
    main()
