from functools import reduce
from operator import mul
import math
import sys

sys.setrecursionlimit(10**9)

# 8 min

def lmap(func, iter):
    return list(map(func, iter))


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def main():
    n = int(input())
    As = lmap(int, input().split())
    As.sort()
    amx = As[-1]
    amid = 0

    for a in As[:-1]:
        if abs(amx - amid*2) > abs(amx - a*2):
            amid = a
        if amx < a*2:
            break

    print(amx, amid)


if __name__ == '__main__':
    main()
