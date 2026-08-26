# Areas on the Cross-Section Diagram


import sys
from collections import deque


def main():
    input_char = list(str(sys.stdin.readline().strip()))
    s1: list[int] = []
    s2: deque[tuple[int, int]] = deque()
    sum: int = 0
    for i, char in enumerate(input_char):
        if char == "\\":
            s1.append(i)
        elif char == "/" and s1:
            j = s1.pop()
            sum += i - j
            a = i - j
            while s2 and s2[-1][0] > j:
                a += s2.pop()[1]
            s2.append((j, a))
    answer: list[int] = []
    while s2:
        answer.append(s2.popleft()[1])
    print(sum)
    print(len(answer), end="")
    for i in answer:
        print(f" {i}", end="")
    print()


if __name__ == "__main__":
    main()
