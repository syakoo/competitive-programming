from functools import reduce
from operator import mul
import math


MOD = 998244353


def lmap(func, iter):
    return list(map(func, iter))


def inv_mod(x: int) -> int:
    return pow(x, MOD-2, MOD)


def cmb_mod(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(lambda x: x[0]*x[1] % MOD, range(n, n - r, -1))
    under = reduce(lambda x: x[0]*x[1] % MOD, range(1, r + 1))
    return (over*inv_mod(under)) % MOD


def cmb(xs: list, r: int) -> int:
    if r == 1:
        return sum(xs) % MOD

    if len(xs) == r:
        return reduce(lambda x: x[0]*x[1] % MOD, xs, 1)

    res = 0
    for i in range(len(xs) - r + 1):
        res += xs[i]*cmb(xs[i+1:], r - 1) % MOD

    return res % MOD


def main():
    n, k = map(int, input().split())
    Ms = lmap(int, input().split())

    Ms.sort()
    p = 0
    for i in range(n-k+1):
        p = (p + cmb_mod(n - i - 1, k - 1) * Ms[i]) % MOD

    q = cmb(Ms, k)
    print(p, q)

    print((p * inv_mod(q)) % MOD)


if __name__ == '__main__':
    main()
