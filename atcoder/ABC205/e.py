# uncleared

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
    n, m, k = map(int, input().split())
    MOD = 10**9 + 7

    mod_cmb = create_mod_cmb(n+m, MOD)
    # 余事象
    comp = 0
    prev = 0
    for i in range(k+1, n+m+1):
        if (i+k-1) % 2 != 0:
            continue

        if (i+k-1)//2 < n:
            tmp = mod_cmb(i-1, (i+k-1)//2)
            comp += (tmp - prev)*mod_cmb(n+m-i, n-(i+k-1)//2-1)
            prev += tmp
            prev %= MOD
            comp %= MOD

    print((mod_cmb(n+m, n) - comp) % MOD)


if __name__ == '__main__':
    main()
