# 30 min
import math
import sys
from operator import mul
from functools import reduce

sys.setrecursionlimit(10**9)


def cmb(n, r):
    if n == 0 or n < r:
        return 0
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def f(n, d):
    return cmb(n, d) * 9 ** d


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = lmap(int, input())
    k = int(input())

    ans = 0
    unzero_cnt = 0
    for i, ni in enumerate(n):
        if ni == 0:
            continue
        unzero_cnt += 1

        if unzero_cnt == k:
            ans += ni + f(len(n)-i-1, k-unzero_cnt+1)
            break

        ans += (ni-1) * f(len(n)-i-1, k-unzero_cnt)
        ans += f(len(n)-i-1, k-unzero_cnt+1)

    print(ans)

if __name__ == '__main__':
    main()
