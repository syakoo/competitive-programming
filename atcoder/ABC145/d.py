# 11 min

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


def lmap(func, iter):
    return list(map(func, iter))


def main():
    x, y = map(int, input().split())
    MOD = 10**9 + 7

    if (x+y) % 3:
        print(0)
        return

    k = (x+y)//3

    if k <= x <= 2*k and k <= y <= 2*k:
        f = create_mod_cmb(k, MOD)

        print(f(k, x-k))
        return

    print(0)


if __name__ == '__main__':
    main()
