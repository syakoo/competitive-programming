from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def create_mod_cmb(n: int, MOD: int):
    """剰余の cmb 🐍(syakoo)

    Args:
        n (int): 最大の n
        MOD (int): 素数、n < MOD

    Returns:
        (n: int, r: int) -> int : 関数 mod_cmb(n, r)
    """
    g1 = [1, 1]
    g2 = [1, 1]

    # O(N lg N) なはず
    for i in range(2, n+1):
        g1.append(g1[i-1]*i % MOD)
        g2.append(g2[i-1]*pow(i, MOD-2, MOD) % MOD)

    def mod_cmb(n: int, r: int) -> int:
        # O(1)
        if r < 0 or r > n:
            return 0
        r = min(r, n-r)
        return g1[n]*g2[r]*g2[n-r] % MOD

    return mod_cmb


print(cmb(6, 1))  # 6
print(cmb(6, 2))  # 15
print(cmb(6, 3))  # 20
print(cmb(6, 4))  # 15
print(cmb(6, 5))  # 6
print(cmb(6, 6))  # 1
