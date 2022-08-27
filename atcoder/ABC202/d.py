import math
from itertools import permutations
from functools import reduce
from operator import mul
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def solve(a, b, k):
    cnt = 0
    for ai in range(a + 1):
        tmp = cmb(b + ai, b)
        if tmp >= k:
            return ai, cnt

        cnt = tmp


def main():
    a, b, k = map(int, input().split())

    ans = []
    while b > 0:
        ai, cnt = solve(a, b, k)
        ans.append('a'*(a - ai)+'b')
        a = ai
        b -= 1
        k -= cnt

    print(''.join(ans) + 'a' * ai)


if __name__ == '__main__':
    main()
