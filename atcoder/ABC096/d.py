import math
import sys
from itertools import combinations

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def compute_primes(n: int) -> list:
    result = []
    for x in range(2, n):
        for y in range(2, int(x**(1/2)) + 1):
            if x % y == 0:
                break
        else:
            result.append(x)

    return result


def main():
    n = int(input())
    primes = compute_primes(55555)
    primes = list(filter(lambda x: x % 5 == 1, primes))
    print(*primes[:n])


if __name__ == '__main__':
    main()
