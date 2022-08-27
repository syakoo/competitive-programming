MOD = 10**9 + 7


def create_mod_cmb(n: int, MOD: int):
    g1 = [1, 1]
    g2 = [1, 1]

    for i in range(2, n+1):
        g1.append(g1[i-1]*i % MOD)
        g2.append(g2[i-1]*pow(i, MOD-2, MOD) % MOD)

    def mod_cmb(n: int, r: int) -> int:
        if r < 0 or r > n:
            return 0
        r = min(r, n-r)
        return g1[n]*g2[r]*g2[n-r] % MOD

    return mod_cmb


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    As = lmap(int, input().split())

    mod_cmb = create_mod_cmb(n, MOD)
    As.sort()
    ans = 0
    for l in range(n-k+1):
        ans -= As[l] * mod_cmb(n-l-1, k-1) % MOD
        ans %= MOD

    for r in range(k-1, n):
        ans += As[r] * mod_cmb(r, k-1) % MOD
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
