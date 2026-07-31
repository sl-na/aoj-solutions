# Graph


from sys import stdin


def main():
    row = int(stdin.readline())
    nl = [[i for i in list(map(int, (line.split())))[2:]] for line in stdin.readlines()]
    columin = max(max(nodes if nodes else [0]) for nodes in nl)
    answer = ""
    for i in range(row):
        for j in range(columin):
            answer += "1" if j + 1 in nl[i] else "0"
            if j != columin - 1:
                answer += " "
            else:
                answer += "\n"
    print(answer, end="")


if __name__ == "__main__":
    main()
