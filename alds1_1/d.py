# Maximum Profit


MAX = 200000


def main():
    n = int(input())
    R = [0] * MAX

    for i in range(n):
        R[i] = int(input())

    maxv = -2000000000
    minv = R[0]

    for i in R[1:n]:
        maxv = max(maxv, i - minv)
        minv = min(minv, i)

    print(maxv)


if __name__ == "__main__":
    main()
