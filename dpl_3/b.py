# Largest Rectangle

import sys


def largest_rectangle(heights):
    stack = []
    max_area = 0
    for i, h in enumerate(heights):
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    while stack:
        height = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)
    return max_area


def build_heights(h, w, c):
    heights = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if c[i][j] == 1:
                heights[i][j] = 0
            else:
                heights[i][j] = (heights[i - 1][j] if 0 < i else 0) + 1
    return heights


def main():
    it = map(int, sys.stdin.read().split())
    h, w = next(it), next(it)
    c = [[next(it) for _ in range(w)] for _ in range(h)]
    heights = build_heights(h, w, c)
    max_area = 0
    for i in range(h):
        max_area = max(max_area, largest_rectangle(heights[i]))
    print(max_area)


if __name__ == "__main__":
    main()
