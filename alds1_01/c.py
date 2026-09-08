# Prime Numbers

import sys
from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    it = map(int, sys.stdin.read().split())
    _ = next(it)
    prime_count = 0
    for n in it:
        if is_prime(n):
            prime_count += 1
    print(prime_count)


if __name__ == "__main__":
    main()
