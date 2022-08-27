def comb_mod(n, r, mod):
    x = 1
    y = 1
    for i in range(r):
        x *= n-i
        y *= i+1
        x %= mod
        y %= mod

    return x*pow(y, mod-2, mod) % mod


MOD = 10 ** 9 + 7


def main():
    m, a, b = map(int, input().split())

    print((pow(2, m, MOD) - 1 - comb_mod(m, a, MOD) - comb_mod(m, b, MOD)) % MOD)


if __name__ == '__main__':
    main()
