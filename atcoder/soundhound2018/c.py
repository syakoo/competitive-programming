# 46 min
from itertools import product
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m, d = map(int, input().split())
    ans = 0
    if d == 0:
        print(1/n * (m-1))
        return

    ans += (n-d) * 2

    print(ans*(m-1) / n**2)


if __name__ == '__main__':
    main()
