# Queue


import sys


class P:
    name: str
    time: int

    def __init__(self, name: str, time: int):
        if len(name) < 1 or len(name) > 10:
            raise ValueError("name length is out of range")
        else:
            self.name = name
        if time < 1 or time > 50000:
            raise ValueError("time is out of range")
        else:
            self.time = time


def main():
    data = sys.stdin.readline().split()
    n = int(data[0])
    q = int(data[1])
    queues: list[P] = []
    for _ in range(n):
        data = sys.stdin.readline().split()
        if len(data) != 2:
            raise ValueError("wrong input data")
        queues.append(P(data[0], int(data[1])))
    if len(queues) != n:
        raise ValueError("queues length is out of range")
    process = 0
    elapsed = 0
    while process < len(queues):
        processing = queues[process]
        process += 1
        run_time = min(q, processing.time)
        processing.time -= run_time
        elapsed += run_time
        if processing.time > 0:
            queues.append(processing)
        else:
            print(processing.name, elapsed)


if __name__ == "__main__":
    main()
