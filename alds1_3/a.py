# Stack


import sys

S = [None] * 1000
top = 0


def push(x):
    global top
    top += 1
    S[top] = x


def pop():
    global top
    top -= 1
    return S[top + 1]


def main():
    for word in sys.stdin.readline().split():
        if word == "+":
            a = pop()
            b = pop()
            push(a + b)
        elif word == "-":
            b = pop()
            a = pop()
            push(a - b)
        elif word == "*":
            a = pop()
            b = pop()
            push(a * b)
        else:
            push(int(word))
    print(pop())


if __name__ == "__main__":
    main()
